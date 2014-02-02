#!/usr/bin/python

import sys
import os
import re
import json
import yaml

def read_modules_file(modules_description_filename):

    modules_description_file = open(modules_description_filename)
    result_map = yaml.load(modules_description_file)

    return result_map

def dump_module_files(modules_directory, result_map):

    for module_name in result_map.keys():
        module_directory = os.path.join(modules_directory, module_name)
        if not os.path.exists(module_directory):
            os.mkdir(module_directory)
        module_file = open(os.path.join(module_directory, 'module.yaml'), 'w')
        module_file.write(yaml.dump(result_map[module_name], indent=4, default_flow_style=False))

    return result_map

def dump_modules_file(modules_directory, result_map):

    with open(os.path.join(modules_directory, 'modules.yaml'), 'w') as f:
        f.write(yaml.dump(result_map, indent=4, default_flow_style=False))

    return result_map

def main():

    if len(sys.argv) != 3:
        print("Usage: process_module_files.py <modules_directory> <modules_description_file>")
        sys.exit(1)

    modules_directory = sys.argv[1]
    modules_description_filename = sys.argv[2]

    result_map = {}
    result_map = read_modules_file(modules_description_filename)
    dump_module_files(modules_directory, result_map)
    dump_modules_file(modules_directory, result_map)

if __name__ == '__main__':
    main()
