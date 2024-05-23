#!/bin/bash

echo -n "Please enter a filename to search: "
read filename



##### file existence test #####
if [ -e $filename ]; then
    echo "file $filename exists."
fi



##### filename test #####
# str1=".sql"
# str2=".dat"


# echo $filename

if [ $( echo "$filename" | grep ".dat" | wc -l ) > 0 ]; then

  
    echo "This is a .dat file."

elif [ $( echo $filename | grep .sql | wc -l ) -eq 1 ]; then

    echo "This is a .sql file."

fi
