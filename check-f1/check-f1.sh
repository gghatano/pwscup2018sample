#!/usr/bin/env sh

dir=$(dirname $0)
cd $dir
python3 -B tool-ncat.py $1 $2 $3 | ruby check-f1.rb
