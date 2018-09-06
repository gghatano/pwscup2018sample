#!/bin/bash

dir=$(dirname $0)
bash $dir/clean.sh

##
python3 $dir/defense.py
python3 $dir/publish.py
python3 $dir/offense.py
python3 $dir/utility.py
python3 $dir/security.py

##
echo '[Utility]' > $dir/result.txt
head $dir/data/out/utility/* >> $dir/result.txt
echo '' >> $dir/result.txt
echo '[Security]' >> $dir/result.txt
head $dir/data/out/security/* >> $dir/result.txt

##
find $dir | grep \\.pyc$ | xargs rm -f
find $dir | grep __pycache__$ | xargs rm -rf
