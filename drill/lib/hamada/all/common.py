# -*- coding: utf-8 -*-

from sys import stdin, stdout, stderr

def read_table(fin = stdin):
    '''
    fin から結合形式を読み込み
    '''
    n = int(fin.readline())
    return list(map(lambda x : fin.readline().rstrip('\n'), range(n)))

def write_table(t, fout = stdout, no_line_num = False):
    '''
    t を fout に結合形式で書き出し
    '''
    if(not no_line_num):
        fout.write(str(len(t)) + '\n')
    for line in t:
        fout.write(line + '\n')

def debug(x):
    stderr.write(str(type(x)) + '\n')
    stderr.write(str(x) + '\n')
