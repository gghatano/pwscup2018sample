# -*- coding: utf-8 -*-
'''
説明:
 有用性を計算

入出力: J(T,A) -> J(U)
'''

from re import match
from math import sqrt
from common import read_table, write_table
from datetime import date
from statistics import mean, pvariance, pstdev

def date2int(d):
    '''
    "yyyy/mm/dd" 形式の年月日を表す文字列を整数に変換
    出力の値は 2010/1/1 からの日数
    '''
    return (date(*map(int, d.split('/'))) - date(2010, 1, 1)).days

def price2int(s):
    '''
    小数点以下2桁までの小数点数x -> 100x (整数)
    '''
    m = match(r"^(\d+)\.(\d\d)$", s)
    if m:
        return int(m.group(1)) * 100 + int(m.group(2))
    m = match(r"^(\d+)\.(\d)$", s)
    if m:
        return int(m.group(1)) * 100 + int(m.group(2)) * 10
    m = match(r"^(\d+)$", s)
    assert m, "invalid num: {}".format(s)
    return int(m.group(1)) * 100

def to_mat(t):
    '''
    ["a,b,c", "d,e,f"] -> [["a", "b", "c"], ["d", "e", "f"]]
    '''
    return [line.split(',') for line in t]

def transpose(mat):
    return [list(x) for x in zip(*mat)]

# assume x \in yset
def mae_set(yset_size):
    return 1.0 - 1.0 / yset_size

# assume x \in [a,b]
def mae_range(x, ab, sd, w = 1):
    a, b = ab
    return float((a - x) ** 2 + (b - x) ** 2 + (b - a) * w) / ((b - a + w) * 2 * sd)

def dist(x, y, del_cost, func_str2num, sd):
    if y == '*': # y が削除
        return del_cost
    if y.startswith('{'): # y が一般化(集合)
        return mae_set(len(y[1:-1].split(';')))
    if y.startswith('['): # y が一般化(区間)
        return mae_range(func_str2num(x), map(func_str2num, y[1:-1].split(';')), sd)
    # assert (func_str2num(x) == func_str2num(y)), "{} == {}".format(x, y)
    return 0.0

def mean_error(tj, aj, del_cost, func_str2num = None, sd = None):
    '''
    概要: j 列の要素ごとの誤差の平均値を計算
    入力:
     tj: T[,j]
     aj: A[,j]
     func_str2num: 文字列表現された D_j の要素を適切な型に変換する関数
     sd: T[,j] の標準偏差
    出力:
     対象列の要素ごとの誤差の平均値
    '''
    return mean(map(lambda ta: dist(*ta, del_cost, func_str2num, sd), zip(tj, aj)))

def il_interval_scale(tj, aj, del_cost, func_str2num):
    '''
    順序尺度用の IL
    '''
    sd = pstdev(list(map(func_str2num, tj)))
    return mean_error(tj, aj, del_cost, func_str2num, sd)

def il_date(tj, aj):
    return il_interval_scale(tj, aj, 1.0, date2int)

def il_item(tj, aj):
    return mean_error(tj, aj, 1.0)

def il_price(tj, aj):
    # mae_range(x, [a,b], sd, w) == mae_range(100 * x, [100 * a, 100 * b], 100 * sd, 100 * w) を利用
    return il_interval_scale(tj, aj, 1.0, price2int)

def il_num(tj, aj):
    return il_interval_scale(tj, aj, 1.0, int)

# input T,A
t = read_table() # T
a = read_table() # A

# T, A を各要素が文字列の二次元配列にし，転置
t = transpose(to_mat(t))
a = transpose(to_mat(a))

# 属性ごとに誤差の平均値を計算して res に追加
res = [
    il_date(t[1], a[1]), # 2列目 (購入日)
    il_item(t[2], a[2]), # 3列目 (商品ID)
    il_price(t[3], a[3]), # 4列目 (単価)
    il_num(t[4], a[4]) # 5列目 (数量)
]

# output U
write_table([str(mean(res))]) # 属性ごとの誤差平均値の平均値を出力
