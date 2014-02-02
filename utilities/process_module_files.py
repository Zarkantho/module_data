#!/usr/bin/python

import sys
import os
import re
import json
import yaml

def split_yaml_version(modules_directory, modules_description_filename):

    modules_description_file = open(modules_description_filename)

    result_map = yaml.load(modules_description_file)

    for module_name in result_map.keys():
        module_directory = os.path.join(modules_directory, module_name)
        if not os.path.exists(module_directory):
            os.mkdir(module_directory)
        module_json_file = open(os.path.join(module_directory, 'module.json'), 'w')
        module_json_file.write(json.dumps(result_map[module_name], indent=4, separators=(',', ': '), sort_keys=True))

    return result_map

def dump_yaml_module_file(modules_directory, result_map):
    with open(os.path.join(modules_directory, 'modules.yaml'), 'w') as f:
        f.write(yaml.dump(result_map, indent=4, default_flow_style=False))

def dump_json_module_file(modules_directory, result_map):
    with open(os.path.join(modules_directory, 'modules.json'), 'w') as f:
        f.write(json.dumps(result_map, indent=4, separators=(',', ': '), sort_keys=True))

def main():

    if len(sys.argv) != 3:
        print("Usage: process_module_files.py <modules_directory> <modules_description_file>")
        sys.exit(1)

    modules_directory = sys.argv[1]
    modules_description_filename = sys.argv[2]

    result_map = {}

    result_map = split_yaml_version(modules_directory, modules_description_filename)

    dump_yaml_module_file(modules_directory, result_map)
    dump_json_module_file(modules_directory, result_map)

main()
