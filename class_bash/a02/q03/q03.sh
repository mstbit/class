#!/bin/bash

./simple.sh > simple.tx
./pinger.sh > pinger.txt
cat simple.txt whoami.txt pinger.txt > q03.txt
