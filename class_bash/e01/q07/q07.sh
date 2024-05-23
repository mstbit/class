#!/bin/bash


###### variable declarations ######
filename1=$1
filename2=$2
# echo check $filename1
# echo check $filename2

###### check parameters ###### 
# if [ -z $filename1 ] || [ -z $filename2 ] ; then

#    echo "Please supply two filenames. Exiting..."
#    exit

# fi

# if [ ! -e $filename1 ] || [ ! -e $filename2 ]; then

#    echo "Please make sure files exist. Exiting..."
#    exit

# fi


######  characgter count and output ######

echo "The character lengths are requested for $filename1 and $filename2"
wc -m $filename1
wc -m $filename2
