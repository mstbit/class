#!/bin/bash
if [ $# -ne 4 ] 
then
	echo "This script requires 4 paramters"
	echo "Usage: ./done.sh fname lname -[A|H|E|P] Assignment_number"
	echo "		fname = your first name"
	echo "		lname = your last name"
	echo "		flag (can be one of the following)"
	echo "			-A = Activity"
	echo "			-E = Exam"
	echo "			-H = Homework"
	echo "			-P = Practice"
	echo "		number = the assignment/exam or homework number"
	exit
fi

fname=$1
lname=$2
num=$4
atype=$3
dir=`pwd`
if [ $num -lt 10 ]
then
  	qn="0""$num"
else
	qn="$num"
fi
if [ $atype = -H ]
then
	file="hwk"
	type="h"
elif [ $atype = -A ]
then
	file="ans"
	type="a"
	cdir="$dir/a""$qn"
elif [ $atype = -E ]
then
	file="exm"
	type="ex"
	cdir="$dir/ex""$num"
elif [ $atype = -P ]
then
	file="pra"
	type="p"
else
	echo "Invalid assignment type provided"
	echo "You entered: $atype"
	echo "The Assignment type must be one of -A, -E, -H, -P"
	exit
fi

if [ $num -lt 10 ]
then
	file="$file""0""$num"".txt"
else
	file="$file""$num"".txt"
fi
if [ -e $file ]
then
	rm $file
fi
if [ $atype = -H ]
then
	check/work.sh $fname $lname $num $type $file
elif [ $atype = -A ]
then
	cd $cdir; $cdir/done.sh $fname $lname $num; cp ans$qn.txt ../ans$qn.txt
elif [ $atype = -E ]
then
	cd $cdir; $cdir/finish.sh $fname $lname $num; cp ans$qn.txt ../exm$qn.txt
fi

