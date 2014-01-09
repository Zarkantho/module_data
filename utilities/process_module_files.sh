#!/bin/bash

for i in mongodb/*/module.txt
do
    NEW_FILE=${i/txt/json}
    python utilities/process_module_files.py $i >> $NEW_FILE
done
