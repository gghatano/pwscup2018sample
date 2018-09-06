# -*- coding: utf-8 -*-
'''
説明:
 A から A' に変換
 A' は A から削除行を除去し，残りを辞書順で整列したもの

入出力: J(A) -> J(A')
'''

from common import read_table, write_table

# input A
a = read_table() # A

# A から削除行を除去
a1 = [x for x in a if not x.startswith('*')]
# 辞書順で整列
a1.sort()

# output A1
write_table(a1)
