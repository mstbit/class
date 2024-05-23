#!/bin/bash

file=$1


# while read line
#    do
#    echo $line
# done < $file

if [ ! -e $file ]; then
  echo "The filename does not exist."
  exit
fi


while :
do

    echo -n 'Please enter the search term: '
    read term

    if [ -z $term ]; then
	echo "Search term not provided. Exiting..."
	exit
    else
        grep -iw $term $file | wc -l
    fi

    echo ""
done
