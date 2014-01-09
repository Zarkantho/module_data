#!/bin/bash

DIR_NAME=""
mkdir mongodb
rm mongodb/general_notes.txt
while read line
do
    case $line in
        \#\#\#\#\#*)
            DIR_NAME=`echo $line | sed 's/#* \(.*\) #*/\1/'`
            mkdir mongodb/$DIR_NAME
            rm mongodb/$DIR_NAME/module.txt
            ;;
    esac
    if [ -z $DIR_NAME ]
    then
        echo $line >> mongodb/general_notes.txt
    else
        echo $line >> mongodb/$DIR_NAME/module.txt
    fi
done < "utilities/project_files.txt"
