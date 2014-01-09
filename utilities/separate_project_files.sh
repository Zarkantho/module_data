#!/bin/bash

DIR_NAME=""
mkdir mongodb
while read line
do
    case $line in
        \#\#\#\#\#*)
            DIR_NAME=`echo $line | sed 's/#* \(.*\) #*/\1/'`
            mkdir mongodb/$DIR_NAME
            ;;
    esac
    if [ -z $DIR_NAME ]
    then
        echo $line >> mongodb/general_notes.txt
    else
        echo $line >> mongodb/$DIR_NAME/module.txt
    fi
done < "project_files.txt"
