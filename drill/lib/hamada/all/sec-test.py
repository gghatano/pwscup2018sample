# -*- coding: utf-8 -*-
'''
説明:
 安全性を計算

入出力: J(R,T,A,F') -> J(S)

Sのフォーマット:
 (0(安全でないとは言えない) または 1(安全でない))
'''

from common import read_table, write_table

def make_pid2oid(t, a):
    '''
    F を作成
    '''
    f = {} # F
    for i, ti in enumerate(t):
        ai = a[i] # A の i 行目
        # ai が削除行だったらスキップ
        if ai.startswith('*'):
            continue
        # ti, ai から顧客IDと仮名をそれぞれ抽出
        oid, pid = map(lambda x : x.split(',')[0], [ti, ai])
        # f の定義域に pid が含まれていなければ，f に pid |--> oid を追加
        if pid not in f:
            f[pid] = oid
    return f

def count_if(seq, condition):
    '''
    contition を満たす seq の要素の数
    '''
    return sum(1 for x in seq if condition(x))

def to_map(r):
    return r

# input R,T,A,F'
r =read_table()   # R
t = read_table()  # T
a = read_table()  # A
f1 = read_table() # F'

r_dict = dict(map(lambda x : x.split(','), r))

f = make_pid2oid(t, a) # F
n = len(f1) # |F'|

# 再識別で当たった数
suc = count_if(map(lambda x : x.split(','), f1), lambda pid_oid : f[pid_oid[0]] == pid_oid[1])

# 出力
s = [
    ('1' if suc >= int(r_dict[str(n)]) else '0'), # 安全でないかどうか
#    str(n), # 再識別試行数
#    str(suc) # 正解数
]

# output S
write_table(s)
