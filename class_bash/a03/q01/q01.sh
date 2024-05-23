#!/bin/bash       
echo "What file would you like to look for (good choices are bin, test, and public_html)"  
read file              # use bin as the default to start, we really want to read this from the terminal

echo "OK, This is a list of where $file was found" > success.log     # This should output to success.log
echo "Oh no!  $file wasn't found here." > error.log                # This should output to error.log

echo "Found $file" >> success.log                                     # This should output to success.log
echo "Did NOT find $file" >> error.log                              # This should output to error.log

for homedir in /home/*; do
    ls --directory --size "$homedir/$file" 1>> success.log 2>> error.log      # This output should go to success.log (if found) or error.log (if not found)
done

