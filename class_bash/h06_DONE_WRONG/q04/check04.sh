#!/bin/bash
dir=`pwd`
flag=`echo $dir|awk '{print match($0,"h06/q04")}'`;
if [ $flag -gt 0 ]
then
	qdir=$dir
else
	qdir=$dir/h06/q04

fi
anum="h06"		# (a|h|e)XX
qnum="q04"		# qXX
rnum="04"		# text for question number
#
#
script=$qdir/check04.sh
script2=$qdir/script04.sh
testing=$( echo $dir | grep -i create | wc -l ) # testing type flag
if [ $testing -eq 1 ]
then
        where=$( echo $dir )
        where=${where/'/h06/q04'//}
        if [ -e $where/testing ]
        then
                testing=1
                cp $script2 $script
        else
                testing=0
        fi
fi
#
#	Set standard functions for checking routines
#
cindex=0
csym=( A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AA AB AC AD AE AF AG AH AI AJ AK AL AM AN AO AP AQ AR AS AT AU AV AW AX AY AZ )

check () {
        setcode
        t=$1
        n=$2
        msg="$3"
        if [ $t -eq 0 ]
        then
                say_OK "$msg"
        else
                say_NOK "$msg" $n
        fi
}

setcode() {
	code="chx""q04-""${csym[$cindex]}"
	cindex=$(( cindex + 1 ))
}
say_OK () {
	main="$1"
	printf "%-10s OK - %s         %25s1\n" " " "$main" $code
}
say_NOK () {
	main="$1"
	printf "%-10s Not OK - %s ( %s ) %25s0\n" " " "$main" $2 $code
}

#
#	Customize this output for the particular script or activity
#



if [ -e $script ]
then
	(
        	cd $qdir

### python file created
                echo "Checking python file $qnum.py"
                msg1="1/5 python file (q04.py) created  "
                v1=1                              # was 3; set to 1; expected value for test 1
                n1=$( ls | grep -iE "$qnum.py" | wc -l )
                t1=$( [ $n1 -ge $v1 ] ; echo $? ) # Modify as needed
                check $t1 $n1 "$msg1"
                echo ""

### 2/5 shebang line exists
                msg2="2/5 shebang line exists           "
                v2=1                              # Set expected value for test 1
                n2=$( cat $qnum.py | grep -E "#!/usr/bin/python*|#!/bin/python*" | wc -l )
                t2=$( [ $n2 -ge $v2 ] ; echo $? ) # Modify as needed
                check $t2 $n2 "$msg2"
                echo ""

### 3/5 user input with input keyword used
                msg3="3/5 user input with input keyword "
                v3=1                              # Set expected value for test 1
                n3=$( cat $qnum.py | grep "input" | wc -l )
                t3=$( [ $n3 -ge $v3 ] ; echo $? ) # Modify as needed
                check $t3 $n3 "$msg3"
                echo ""

### type conversion function int( ) used
                echo "Cheking type conversion"
                msg4="4/5 type conversion & if-else     "
                v4=1
		x4=1
		y4=1
		z4=1
                n4=$( cat $qnum.py | grep "str" | grep -v ^# | wc -l )
                a4=$( cat $qnum.py | grep "if" | wc -l )
                b4=$( cat $qnum.py | grep "else" | wc -l )
                t4=$( [ $n4 -eq $v4 ] && [ $a4 -eq $x4 ] && [ $b4 -eq $y4 ] ; echo $? ) # Modify as needed
                check $t4 $n4 "$msg4"
                echo ""

### script output
                msg5="5/5 running python code...        "
                v5=1
		a5=5
		# py='q04.py'
                n5=$( echo $a5 | python3 $qnum.py | grep 'have entered an integer' | wc -l )
                t5=$( [ $n5 -eq $v5 ]; echo $?)
                check $t5 $n5 "$msg5"
                echo ""






	)
else
	echo "$script not found - INCOMPLETE SOLUTION"
fi

###
