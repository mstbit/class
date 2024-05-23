#!/bin/bash

##### define alias
alias accounts='ls /home'

##### define ENVs
export Q2='/home/chen_user/class/h03/q02'
export WEB=~/public_html

##### define functions
### extract
### might be attempted to place num=$1 here
function extract () {
  num=$1	### use local variable here because functions are individual subroutines to be called separately
  tar -xvf a0$num.tar.gz > t$num.txt

}

### cleanup
function cleanup () {
  num=$1
  rm t$num.txt
  rm -rf a0$num

}
