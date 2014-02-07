#!/usr/bin/python

import sys
import os
import re
import json
import yaml

from data_access import read_project_structure_file, dump_module_files, write_project_structure_file

def main():

    if len(sys.argv) != 2:
        print("Usage: process_module_files.py <modules_directory>")
        sys.exit(1)

    project_data_directory = sys.argv[1]
    result_map = read_project_structure_file(project_data_directory)
    dump_module_files(project_data_directory, result_map)

if __name__ == '__main__':
    main()
