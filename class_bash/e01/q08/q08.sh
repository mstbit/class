#!/bin/bash

###### read input and variable declaration #####
echo -n "Please enter a filename: "
read filename



###### check file existence and output  ######
if [ -e $filename ] ; then 
    echo "File exists"
    echo $filename
    grep -iw "good" $filename
else 
    echo "The file $filename does not exist. Exiting..."
    exit
fi
