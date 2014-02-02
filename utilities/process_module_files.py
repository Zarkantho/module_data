#!/usr/bin/python

import sys
import os
import re
import json
import yaml

def read_modules_file(modules_description_filename):

    modules_description_file = open(modules_description_filename)
    result_map = yaml.load(modules_description_file)

    print result_map

    return result_map

def dump_module_files(base_directory, result_map):

    for system_name in result_map.keys():
        system_directory = os.path.join(base_directory, system_name)
        if not os.path.exists(system_directory):
            os.mkdir(system_directory)
        for module_object in result_map[system_name]['modules']:
            module_directory = os.path.join(system_directory, module_object['name'])
            if not os.path.exists(module_directory):
                os.mkdir(module_directory)
            module_file = open(os.path.join(module_directory, 'module.yaml'), 'w')
            module_file.write(yaml.dump(module_object, indent=4, default_flow_style=False))

    return result_map

# TODO: Actually preserve the ordering as I dump the YAML file.  See
# http://stackoverflow.com/questions/8651095/controlling-yaml-serialization-order-in-python
def dump_modules_file(base_directory, result_map):

    with open(os.path.join(base_directory, 'modules.yaml'), 'w') as f:
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
    #dump_modules_file(modules_directory, result_map)

if __name__ == '__main__':
    main()
