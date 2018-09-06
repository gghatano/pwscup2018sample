# -*- coding: utf-8 -*-
'''
実行方法:
 $ python3 ano-del-lc.py [p = 0.5]

説明:
 T の各要素を確率 p で削除

入出力: J(T) -> J(A)
'''

from common import read_table, write_table
from random import random
from sys import argv

def del_by_p(s, p):
    '''
    s の各要素を確率 p で削除
    '''
    return ','.join([('*' if random() < p else x) for x in  s.split(',')])

# 削除確率をコマンドライン引数から読み込み．指定しない場合 0.5
del_rate = 0.5
if len(argv) > 1:
    del_rate = float(argv[1])

# input T
t = read_table()

# 各セルを確率 del_rate で削除
t = list(map(lambda x: del_by_p(x, del_rate), t))
# IDが削除されている場合，同じ行の他の要素も削除
t = [('*,*,*,*,*' if x.startswith('*') else x) for x in t]

# output A
write_table(t)
