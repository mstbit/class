#!/bin/bash
tar -xvf web.tar.gz --wildcards "*.html"

grep -i href *.html web/*.html 2>/dev/null
