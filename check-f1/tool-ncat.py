# -*- coding: utf-8 -*-
'''
説明:
 指定されたファイルを順に読み込んで結合形式で出力
 
実行方法:
 $ python3 tool-ncat.py FILE_1 FILE_2 ... FILE_n

出力:
 (FILE_1の行数)
 (FILE_1の中身)
 (FILE_2の行数)
 (FILE_2の中身)
 ...
 (FILE_nの行数)
 (FILE_nの中身)
'''

from sys import argv
from common import write_table

for i, fname in enumerate(argv):
    if(i == 0):
        continue
    with open(fname, 'r') as fin:
        write_table([x.rstrip('\n') for x in fin.readlines()])
