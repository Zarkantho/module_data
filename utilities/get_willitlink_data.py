from willitlink.base.graph import MultiGraph
from willitlink.base.dev_tools import Timer

from willitlink.queries.find_interface import find_interface
from willitlink.queries.libstats import resolve_leak_info
from willitlink.queries.executables import get_executable_list

import sys
import json
import os
import re

import willitlink

willitlink_location = os.path.dirname(willitlink.__file__)
default_data_file = os.path.join(willitlink_location, os.pardir, 'data', "dep_graph.json")

# Returns a hash of all modules
def get_module_data(modules_directory):
    module_directories = os.listdir(modules_directory)
    module_data = {}
    for module_directory in module_directories:
        if os.path.isdir(os.path.join(modules_directory, module_directory)):
            module_data[module_directory] = json.load(open(os.path.join(modules_directory,
                                                           module_directory,
                                                           "module.json")))
    return module_data

# The modules have files listed in "groups".  This returns a list of all files for the module.
def get_module_files(single_module_data):
    module_files = []
    for module_group in single_module_data['groups']:
        module_files.extend(module_group['files'])
    return module_files

# The modules have files listed in "groups".  This adds a 'files_flat' entry to each module that has
# a list of all files for the module.
def add_files_list(module_data):
    for module_name in module_data.keys():
        module_data[module_name]['files_flat'] = get_module_files(module_data[module_name])

def load_graph(data_file):
    with Timer('loading graph', False):
        g = MultiGraph(timers=False).load(data_file)
    return g

def object_files(source_files):
    source_match_regex = re.compile(r"^.*((:?(:?mongo)|(:?client_build)|(:?third_party)).*\.)c[pc]?[p]?")
    object_files = []
    for source_file in source_files:
        source_match = source_match_regex.match(source_file)
        if source_match:
            object_files.append(source_match.group(1) + "o")
    return object_files

def object_file_to_source_file(graph, object_file):
    object_match_regex = re.compile(r"^.*((:?(:?mongo)|(:?client_build)|(:?third_party)).+\.)o$")
    object_match = object_match_regex.match(object_file)
    for i in graph.files:
        if i.endswith(object_match.group(1) + "cpp") or i.endswith(object_match.group(1) + "c") or i.endswith(object_match.group(1) + "cc"):
            return i

def source_files(graph, object_files):
    source_files = []
    for object_file in object_files:
        source_files.append(object_file_to_source_file(graph, object_file))
    return source_files

def add_interface_data(graph, module_data):
    for module_name in module_data.keys():
        module_data[module_name]['interface'] = find_interface(graph, object_files(module_data[module_name]['files_flat']))
        for interface_object in module_data[module_name]['interface']:
            interface_object['object'] = source_files(graph, [interface_object['object']])[0]
            interface_object['used_by'] = source_files(graph, interface_object['used_by'])

def add_leak_data(graph, module_data):
    for module_name in module_data.keys():
        module_data[module_name]['leaks'] = resolve_leak_info(graph, object_files(module_data[module_name]['files_flat']), 1, None, [])
        for leak_object in module_data[module_name]['leaks']:
            leak_object['object'] = source_files(graph, [leak_object['object']])[0]
            leak_object['sources'] = source_files(graph, leak_object['sources'].keys())

def add_executable_data(graph, module_data):
    for module_name in module_data.keys():
        module_data[module_name]['files_with_exec'] = []
        for object_file in object_files(module_data[module_name]['files_flat']):
            module_data[module_name]['files_with_exec'].append({ "name" : object_file_to_source_file(object_file), "execs" : get_executable_list(graph, [object_file]) })

def output_detailed_module_data(modules_directory, module_data):
    module_directories = os.listdir(modules_directory)
    for module_directory in module_directories:
        if os.path.isdir(os.path.join(modules_directory, module_directory)):
            # Put data about the interface
            f = open(os.path.join(modules_directory, module_directory, "interface.json"), 'w')
            f.truncate()
            f.write(json.dumps(module_data[module_directory]['interface'], indent=4))
            # Put data about the leaks
            f = open(os.path.join(modules_directory, module_directory, "leaks.json"), 'w')
            f.truncate()
            f.write(json.dumps(module_data[module_directory]['leaks'], indent=4))
            # Put data about the files_with_exec
            f = open(os.path.join(modules_directory, module_directory, "files_with_exec.json"), 'w')
            f.truncate()
            f.write(json.dumps(module_data[module_directory]['files_with_exec'], indent=4))

def main():

    if len(sys.argv) != 2:
        print "Usage: <module_files>"
        exit(1)

    module_data = get_module_data(sys.argv[1])
    add_files_list(module_data)
    graph = load_graph(default_data_file)

    add_interface_data(graph, module_data)
    add_leak_data(graph, module_data)
    add_executable_data(graph, module_data)

    output_detailed_module_data(sys.argv[1], module_data)

if __name__ == '__main__':
    main()
