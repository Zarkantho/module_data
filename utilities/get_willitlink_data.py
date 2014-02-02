from willitlink.base.graph import MultiGraph
from willitlink.base.dev_tools import Timer

from willitlink.queries.find_interface import find_interface
from willitlink.queries.libstats import resolve_leak_info
from willitlink.queries.executables import get_executable_list

import sys
import json
import os
import re

from process_module_files import read_modules_file

import willitlink

def dbgprint(my_object):
    print json.dumps(my_object, indent=4)

def get_project_data(base_directory):
    return read_modules_file(os.path.join(base_directory, "modules.yaml"))

# The modules have files listed in "groups".  This returns a list of all files for the module.
def get_module_files(single_module_data):
    module_files = []
    for module_group in single_module_data['groups']:
        module_files.extend(module_group['files'])
    return module_files

# The modules have files listed in "groups".  This adds a 'files_flat' entry to each module that has
# a list of all files for the module.
def add_files_list(project_data):
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            module_object['files_flat'] = get_module_files(module_object)

def load_graph(data_file):
    with Timer('loading graph', False):
        g = MultiGraph(timers=False).load(data_file)
    return g

# The following four *_file_to_*_file(s) functions convert to/from *.o and *.cpp files.
# TODO:  If we use the "client_build" and the server build, this function will return more than one
# value for what the object file is.  However, the data in this repo is currently generated from
# both.  We should have only the server objects or only the client objects, since they are
# essentially two completely independent builds.
def source_file_to_object_file(graph, source_file):
    # TODO: Make this an assertion or something more obvious
    object_files = graph.get('source_to_file', source_file)
    if (len(object_files)) > 1:
        print object_files
    return object_files

def source_files_to_object_files(graph, source_files):
    object_files = []
    for source_file in source_files:
        object_files.extend(source_file_to_object_file(graph, source_file))
    return object_files

def object_file_to_source_file(graph, object_file):
    source_files = graph.get('file_to_source', object_file)
    if (len(source_files)) > 1:
        print source_files
    return source_files

def object_files_to_source_files(graph, object_files):
    source_files = []
    for object_file in object_files:
        source_files.extend(object_file_to_source_file(graph, object_file))
    return source_files

def add_interface_data(graph, project_data):
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            module_object['interface'] = find_interface(graph, source_files_to_object_files(graph, module_object['files_flat']))
            for interface_object in module_object['interface']:
                interface_object['object'] = object_files_to_source_files(graph, [interface_object['object']])[0]
                interface_object['used_by'] = object_files_to_source_files(graph, interface_object['used_by'])

def add_leak_data(graph, project_data):
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            module_object['leaks'] = resolve_leak_info(graph, source_files_to_object_files(graph, module_object['files_flat']), 1, None, [])
            for leak_object in module_object['leaks']:
                leak_object['object'] = object_files_to_source_files(graph, [leak_object['object']])[0]
                leak_object['sources'] = list(set(object_files_to_source_files(graph, leak_object['sources'].keys())))

def add_executable_data(graph, project_data):
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            module_object['files_with_exec'] = []
            for source_file in module_object['files_flat']:
                executable_list = []
                executable_list = get_executable_list(graph, source_file)
                module_object['files_with_exec'].append({ "name" : source_file, "execs" : executable_list })

# Builds a map of source files to modules
def build_file_to_module_map(project_data):
    file_to_module = {}
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            for module_file in module_object['files_flat']:
                file_to_module[module_file] = module_object['name']
    return file_to_module

# Builds a map of source files to executables
def build_file_to_executables_map(project_data):
    file_to_executables = {}
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            for file_with_exec in module_object['files_with_exec']:
                if (file_with_exec["name"] is not None):
                    file_to_executables[file_with_exec['name']] = file_with_exec['execs']
    return file_to_executables

# Builds a map of source files to interface
def build_file_to_interface_map(project_data):
    file_to_interface = {}
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            for interface_object in module_object['interface']:
                file_name = interface_object['object']
                if file_name not in file_to_interface:
                    file_to_interface[file_name] = []
                file_to_interface[file_name].append(interface_object)
    return file_to_interface

# Builds a map of source files to dependencies
def build_file_to_dependencies_map(project_data):
    file_to_dependencies = {}
    for system_name in project_data.keys():
        for module_object in project_data[system_name]['modules']:
            for dependencies_object in module_object['leaks']:
                file_name = dependencies_object['object']
                if file_name not in file_to_dependencies:
                    file_to_dependencies[file_name] = []
                file_to_dependencies[file_name].append(dependencies_object)
    return file_to_dependencies

# Simplifies the list of executables into something more readable.
#
# Example:
# [ "mongod", "mongos", "mongotop", "mongodump", "mongoexport", "mongoimport", "mongobridge",
# "mongoperf", "bsondump", "mongofiles", "mongosniff", "mongorestore", "mongostat", "mongooplog" ]
#
# Turns into:
#
# [ "mongod", "mongos", "tools" ]
def get_exec_digest(exec_list):
    supported_binaries = [ "mongod", "mongos" ]
    tool_binaries = [ "mongotop", "mongodump", "mongoexport", "mongoimport", "mongobridge",
            "mongoperf", "bsondump", "mongofiles", "mongosniff", "mongorestore", "mongostat",
            "mongooplog" ]
    dbtests = [ "test", "perftest" ]
    client_examples = ["firstExample", "rsExample", "authTest", "httpClientTest", "tutorial", "clientTest", "whereExample", "secondExample" ]

    exec_digest = set()
    for exec_name in exec_list:
        if exec_name in supported_binaries:
            exec_digest.add(exec_name)
        if exec_name in tool_binaries:
            exec_digest.add("tools")
        if exec_name in client_examples:
            exec_digest.add("cppclientdriver")
        # Do nothing if exec_name in dbtests

    return list(exec_digest)

# Outputs a README.md file for each system with some useful information
def output_readme_files_for_systems(project_directory, project_data):
    for system_name in project_data.keys():
        system_directory = os.path.join(project_directory, system_name)

        top_level_readme = open(os.path.join(system_directory, "README.md"), 'w')
        top_level_readme.truncate()

        # Add the header for this system
        markdown_sanitized_system_name = system_name.replace("_", "\\_")
        top_level_readme.write("# " + markdown_sanitized_system_name + "\n\n")

        # TODO: add the description for this system

        # Output module information for this system
        top_level_readme.write("## Modules\n\n")
        for module_object in project_data[system_name]['modules']:
            module_path = os.path.join(system_directory, module_object['name'])
            if os.path.isdir(module_path):

                # Sanitize the module name for this sytem readme
                markdown_sanitized_module_name = module_object['name'].replace("_", "\\_")

                # Heading for this module
                top_level_readme.write("### " + markdown_sanitized_module_name + "\n\n")

                # Files in this module
                for source_file in module_object['files_flat']:
                    markdown_sanitized_source_file = source_file.replace("_", "\\_")
                    top_level_readme.write("- [" + markdown_sanitized_source_file + "](" + markdown_sanitized_module_name + ")" + "\n")


# Outputs a README.md file for each module with some useful information
def output_readme_files_for_modules(project_directory, project_data):
    file_to_executables = build_file_to_executables_map(project_data)
    file_to_interface = build_file_to_interface_map(project_data)
    file_to_dependencies = build_file_to_dependencies_map(project_data)
    file_to_module = build_file_to_module_map(project_data)

    for system_name in project_data.keys():
        modules_directory = os.path.join(project_directory, system_name)

        for module_object in project_data[system_name]['modules']:
            module_path = os.path.join(modules_directory, module_object['name'])
            if os.path.isdir(module_path):

                f = open(os.path.join(module_path, "README.md"), 'w')
                f.truncate()
                # First, the title of the module
                f.write("# " + module_object['name'].replace("_", "\\_") + "\n\n")

                f.write("# Module Groups\n")

                # Do the following analysis for each group separately
                for module_group in module_object['groups']:

                    # Horizontal rule
                    f.write("\n-------------\n\n")

                    # Comments for this group of files
                    f.write("# Group Description\n")
                    f.write(module_group["comments"].replace("#", " ").replace("_", "\\_").lstrip() + "\n\n")

                    # Files in this module group
                    f.write("# Files\n")
                    for file_name in module_group["files"]:
                        f.write("- " + file_name.replace("_", "\\_"))
                        if file_name in file_to_executables:
                            file_to_executables[file_name]
                            f.write("   (" + ", ".join(get_exec_digest(file_to_executables[file_name])) + ")\n")
                        else:
                            f.write("\n")

                    # Interface for this module group (symbols used from outside this module)
                    f.write("\n# Interface\n")
                    something_in_interface = False
                    for file_name in module_group["files"]:
                        if file_name in file_to_interface:
                            something_in_interface = True
                            f.write("\n### " + file_name.replace("_", "\\_") + "\n")
                            for interface_object in file_to_interface[file_name]:
                                f.write("\n<div></div>\n") # This is a weird markdown idiosyncrasy to
                                                        # make sure the indented block with the symbol
                                                        # is interpreted as a literal block
                                f.write("\n    " + interface_object['symbol'] + "\n\n")
                                f.write("- Used By:\n\n")
                                for file_using in interface_object['used_by']:
                                    if file_using in file_to_module:
                                        f.write("    - [" + file_using.replace("_", "\\_") + "](../" + file_to_module[file_using].replace("_", "\\_") + ")" + "\n")
                                    else:
                                        f.write("    - " + file_using.replace("_", "\\_") + "\n")
                    if not something_in_interface:
                        f.write("(not used outside this module)\n")

                    # Dependencies for this module group (symbols used that are defined outside this module)
                    f.write("\n# Dependencies\n")
                    something_in_dependencies = False
                    for file_name in module_group["files"]:
                        if file_name in file_to_dependencies:
                            something_in_dependencies = True
                            f.write("\n### " + file_name.replace("_", "\\_") + "\n")
                            for dependencies_object in file_to_dependencies[file_name]:
                                f.write("\n<div></div>\n") # This is a weird markdown idiosyncrasy to
                                                        # make sure the indented block with the symbol
                                                        # is interpreted as a literal block
                                f.write("\n    " + dependencies_object['symbol'] + "\n\n")
                                f.write("- Provided By:\n\n")
                                for file_providing in dependencies_object['sources']:
                                    if file_providing in file_to_module:
                                        f.write("    - [" + file_providing.replace("_", "\\_") + "](../" + file_to_module[file_providing].replace("_", "\\_") + ")" + "\n")
                                    else:
                                        f.write("    - " + file_providing.replace("_", "\\_") + "\n")
                    if not something_in_dependencies:
                        f.write("(no dependencies outside this module)\n")

def output_detailed_module_data(project_directory, project_data):
    for system_name in project_data.keys():
        modules_directory = os.path.join(project_directory, system_name)
        for module_object in project_data[system_name]['modules']:
            if os.path.isdir(os.path.join(modules_directory, module_object['name'])):
                # Put data about the interface
                f = open(os.path.join(modules_directory, module_object['name'], "interface.json"), 'w')
                f.truncate()
                f.write(json.dumps(module_object['interface'], indent=4))
                # Put data about the leaks
                f = open(os.path.join(modules_directory, module_object['name'], "leaks.json"), 'w')
                f.truncate()
                f.write(json.dumps(module_object['leaks'], indent=4))
                # Put data about the files_with_exec
                f = open(os.path.join(modules_directory, module_object['name'], "files_with_exec.json"), 'w')
                f.truncate()
                f.write(json.dumps(module_object['files_with_exec'], indent=4))

def main():

    if len(sys.argv) != 2:
        print "Usage: <base_directory>"
        exit(1)

    base_directory = sys.argv[1]

    project_data = get_project_data(base_directory)
    add_files_list(project_data)
    graph = load_graph(os.path.join(base_directory, 'willitlink-data', 'dep_graph.json'))

    add_interface_data(graph, project_data)
    add_leak_data(graph, project_data)
    add_executable_data(graph, project_data)

    output_detailed_module_data(base_directory, project_data)
    output_readme_files_for_systems(base_directory, project_data)
    output_readme_files_for_modules(base_directory, project_data)

if __name__ == '__main__':
    main()

