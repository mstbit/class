#!/bin/bash

tar -xf web.tar.gz --wildcards *.html

grep -i href *.html web/*html 2>/dev/null
# grep -r -i 'href' ~/class/h03/q01
