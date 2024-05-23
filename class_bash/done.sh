#!/bin/bash
fname=$1
lname=$2
assignment=$3
if [ "$#" -ne 3 ]
then
	echo "${BASH_SOURCE[0]}	- requires 3 parameters"
	echo "			- your first name"
	echo "			= your last name"
	echo "			- the name of the assignment"
else
	dir=$(pwd)
	program=$dir/done/done.pl
	echo "Calling $program $fname $lname $assignment"
	$program $fname $lname $assignment
	( cd $dir/$assignment

	  	file=$(ls -1 *.txt)
		if [ -n "$file" ]
		then
		  	if [ -f "$file" ]
		  	then
				newfile=${file/txt/dat}
				cp $file $newfile
				echo ""
				echo "Copy of $file put in $newfile"
			fi
		else
			type=$( echo ${assignment:0:1} )
			id=$( echo ${assignment:1:2} )
			if [ "$type" == "h" ]
			then
				newfile="hwk$id.txt"
			fi
			if [ "$type" == "a" ]
			then
				newfile="lab$id.txt"
			fi
			if [ "$type" == "e" ]
			then
				newfile="exm$id.txt"
			fi
			touch $newfile
			echo ""
			echo "Empty file in $newfile"
		fi
	)
fi
