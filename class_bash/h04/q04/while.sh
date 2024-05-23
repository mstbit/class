#!/bin/bash

file=test.in

while read var; do

    echo $var

done < $file
