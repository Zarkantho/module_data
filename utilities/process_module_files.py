#!/usr/bin/python

# Get Arguments
import sys

import re
import json

def main():

    if len(sys.argv) != 2:
        print("Usage: process_module_files.py <module_file>")
        sys.exit(1)

    title_regex = re.compile("^#+ (.*) #+")
    comment_regex = re.compile("^(#+.*)")
    source_file_regex = re.compile("(src\S*)(:?.*)?")

    module_filename = sys.argv[1]
    module_file = open(module_filename)

    result_map = {}
    result_map["groups"] = []
    current_comments = ""
    current_files = []

    for line in module_file:
        title_match = title_regex.match(line)
        comment_match = comment_regex.match(line)
        source_file_match = source_file_regex.match(line)
        if title_match:
            result_map["title"] = title_match.group(1)
            continue
        if comment_match:
            # We are starting a new section
            if len(current_files) > 0:
                group_map = {}
                group_map["files"] = current_files
                group_map["comments"] = current_comments
                result_map["groups"].append(group_map)
                current_files = []
                current_comments = ""
            current_comments = current_comments + comment_match.group(1)
            continue
        if source_file_match:
            current_files = current_files + [ source_file_match.group(1) ]
            continue
    group_map = {}
    group_map["files"] = current_files
    group_map["comments"] = current_comments
    result_map["groups"].append(group_map)

    print json.dumps(result_map, indent=4, separators=(',', ': '))

main()
