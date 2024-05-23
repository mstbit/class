

#### alias accounts
alias accounts='ls /home'


### ENV
export Q2=~/class/h03/q02
export WEB=~/public_html

### function extract clean
function extract (){

  num=$1
  tar -xvf a0${num}.tar.gz > t${num}.txt

}

function cleanup(){

  num=$1
  rm t${num}.txt
  rm -rf a0${num}



}

