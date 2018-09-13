#!/usr/bin/env sh

python3 tool-ncat.py $1 $2 $3 | ruby check-f1.rb
