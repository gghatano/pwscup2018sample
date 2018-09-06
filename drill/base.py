#!/usr/bin/env python3
#
# base.py

from os import getcwd, makedirs
from re import match, split
from shutil import rmtree
from subprocess import PIPE, Popen

class Base():
    cwd = getcwd()
    tr = 'data/T.csv'
    r_csv = 'data/R.csv'
    #ncat = 'ruby {cwd}/lib/hamada/tools/ncat.rb'.format(cwd=cwd)
    #nsplit = 'ruby {cwd}/lib/hamada/tools/nsplit.rb'.format(cwd=cwd)
    ncat = 'python3 {cwd}/lib/hamada/all/tool-ncat.py'.format(cwd=cwd)
    nsplit = 'python3 {cwd}/lib/hamada/all/tool-nsplit.py'.format(cwd=cwd)
    dir_lib = 'lib'
    dir_out = 'data/out'
    debug_level = 3

    def mkdir_p(self, dir):
	## ディレクトリの強制作成
        try:
            makedirs(dir)
        except:
            pass

    def write(self, buf, fout):
        ## バッファをファイル出力
        if len(buf) > 0:
            with open(fout, 'w') as fo:
                fo.writelines(str(buf))

    def read_l_t_player_method_cmd(self, file_input, side):
        ## 参加者情報の読み込み
        from csv import reader
        l_t_player_method_cmd = []
        with open(file_input) as fi:
            for row in reader(fi): 
                if row == [] or row[0].strip()[0] == '#':
                    continue
                row = [str(elm.strip()) for elm in row]
                if row[0] == side:
                    l_t_player_method_cmd.append(tuple(row[1:]))
        return l_t_player_method_cmd

    def do_shell(self, cmd, cwd, fout, ferr):
	## 外部プログラムの実行
        p = Popen(cmd, shell = True, stdout = PIPE, stderr = PIPE, cwd = cwd)
        stdout, stderr = p.communicate()
        self.write(stdout, fout)
        self.write(stderr, ferr)
        if len(stderr) > 0:
            print("*** Some stderr appeared. ***")
            print(stderr)

    def print_cmd(self, cmd, twd=''):
        if self.debug_level >= 2:
            print('[' + twd + '] ' + cmd)
