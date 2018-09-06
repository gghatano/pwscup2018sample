# -*- coding: utf-8 -*-
'''
説明:
 結合形式の各パートをファイルに順に出力
 
実行方法:
 $ python3 tool-nsplit.py FILE_1 FILE_2 ... FILE_n
'''

from sys import argv
from common import write_table, read_table

for i, fname in enumerate(argv):
    if(i == 0):
        continue
    with open(fname, 'w') as fout:
        write_table(read_table(), fout, True)
