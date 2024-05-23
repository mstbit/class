#!/bin/bash


###### declare variable ######
file1=$1
file2=$2
file3=$3

if [ ! -e headers ]; then
   touch headers.txt
fi

output=headers.txt
cat /dev/null > $output


###### file existence test ######


if [ ! -e $file1 ]; then
    echo File $file1 does not exist. Existing...
else 
    echo "File $file1 exists"
    head -n 3 $file1 > $output
fi


if [ ! -e $file2 ]; then
    echo "File $file2 does not exist. Existing..."
else 
    echo File $file2 exists
    head -n 3 $file2 >> $output
fi


if [ ! -e $file3 ]; then
    echo "File $file3 does not exist"
else 
    echo File $file3 exists
    head -n 3 $file3 >> $output
fi
