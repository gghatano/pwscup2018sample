#!/bin/bash

rm -rf ./data/out
rm ./data/result.txt
find . | grep \\.pyc$ | xargs rm -f
find . | grep \~$ | xargs rm -f
find . | grep __pycache__$ | xargs rm -rf
