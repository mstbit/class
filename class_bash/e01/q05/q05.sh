#!/bin/bash


##### href search ######
grep -i href in*.html > hrefs.txt
grep -iE "jpg|jpeg|gif" in*html > pics.txt
cat hrefs.txt | wc -l
cat pics.txt | wc -l
grep -i .gif *.html | wc -l
