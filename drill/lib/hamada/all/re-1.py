# -*- coding: utf-8 -*-
'''
実行方法:
 $ python3 re-1.py

説明:
 A' で最初に出現する仮名を T の最初に出現する仮名と推測

入出力: J(T, A') -> J(F')
'''

from common import read_table, write_table

def to_ids(t):
    '''
    1列目の要素を抜き出す
    '''
    return [x.split(',')[0] for x in t]

# input T,A'
t = read_table()
a1 = read_table()

oids = to_ids(t)
pids = to_ids(a1)

f1 = ['{},{}'.format(pids[0], oids[0])]

# output F'
write_table(f1)
