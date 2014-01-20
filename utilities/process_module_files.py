#!/usr/bin/python

import sys
import os
import re
import json
import yaml

def split_txt_version(modules_directory, modules_description_filename):
    title_regex = re.compile("^#+ (.*) #+")
    comment_regex = re.compile("^(#+.*)")
    source_file_regex = re.compile("((:?(:?src)|(:?build))\S*)(:?.*)?")

    result_map = {}
    current_comments = ""
    current_files = []
    current_module = ""

    module_file = open(os.path.join(modules_directory, 'general_notes.txt'), 'w')
    modules_description_file = open(modules_description_filename)

    # This loop is doing two things (maybe they could be separated)
    # 1. Building the "result_map" object
    # 2. Building a "modules.txt" file in each module directory
    for line in modules_description_file:
        title_match = title_regex.match(line)
        comment_match = comment_regex.match(line)
        source_file_match = source_file_regex.match(line)

        if title_match:

            # We are starting a new module, so add the current state to the previous one
            if len(current_module) > 0:
                group_map = {}
                group_map["files"] = current_files
                group_map["comments"] = current_comments
                result_map[current_module]["groups"].append(group_map)
                current_files = []
                current_comments = ""

            current_module = title_match.group(1)
            module_directory = os.path.join(modules_directory, current_module)
            if not os.path.exists(module_directory):
                os.mkdir(module_directory)
            module_file = open(os.path.join(modules_directory, current_module, 'module.txt'), 'w')
            result_map[current_module] = {}
            result_map[current_module]["groups"] = []
            result_map[current_module]["title"] = current_module
        elif comment_match:
            # We are starting a new section, so add the current state to this module and reset
            if len(current_files) > 0:
                group_map = {}
                group_map["files"] = current_files
                group_map["comments"] = current_comments
                result_map[current_module]["groups"].append(group_map)
                current_files = []
                current_comments = ""

            # Only aggregate comments if we are in a module
            if len(current_module) > 0:
                current_comments = current_comments + comment_match.group(1)
        elif source_file_match:
            current_files = current_files + [ source_file_match.group(1) ]

        module_file.write(line)

    group_map = {}
    group_map["files"] = current_files
    group_map["comments"] = current_comments
    result_map[current_module]["groups"].append(group_map)

    for module_name in result_map.keys():
        module_json_file = open(os.path.join(modules_directory, module_name, 'module.json'), 'w')
        module_json_file.write(json.dumps(result_map[module_name], indent=4, separators=(',', ': ')))

    return result_map

def split_yaml_version(modules_directory, modules_description_filename):

    modules_description_file = open(modules_description_filename)

    result_map = yaml.load(modules_description_file)

    for module_name in result_map.keys():
        module_json_file = open(os.path.join(modules_directory, module_name, 'module.json'), 'w')
        module_json_file.write(json.dumps(result_map[module_name], indent=4, separators=(',', ': ')))

    return result_map

def main():

    if len(sys.argv) != 3:
        print("Usage: process_module_files.py <modules_directory> <modules_description_file>")
        sys.exit(1)

    modules_directory = sys.argv[1]
    modules_description_filename = sys.argv[2]

    # TODO: Actually do some processing before I output the files here
    if modules_description_filename.endswith(".yaml"):
        with open(os.path.join(modules_directory, 'modules.json'), 'w') as f:
            f.write(json.dumps(split_yaml_version(modules_directory, modules_description_filename), indent=4, separators=(',', ': ')))
        with open(os.path.join(modules_directory, 'modules.yaml'), 'w') as f:
            f.write(yaml.dump(split_yaml_version(modules_directory, modules_description_filename), indent=4))
    else:
        with open(os.path.join(modules_directory, 'modules.json'), 'w') as f:
            f.write(json.dumps(split_txt_version(modules_directory, modules_description_filename), indent=4, separators=(',', ': ')))
        with open(os.path.join(modules_directory, 'modules.yaml'), 'w') as f:
            f.write(yaml.dump(split_txt_version(modules_directory, modules_description_filename), indent=4))

main()
