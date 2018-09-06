#!/usr/bin/env python3
#
# defense.py
#
# [USAGE] python3 defense.py [player.csv]

from sys import argv
from base import Base

class Defense(Base):
    def __init__(self, file_player):
        self.dir_data = self.dir_out + '/defense'
        self.l_t_player_method_cmd = self.read_l_t_player_method_cmd(file_player, 'defense')

    def get_fname(self, player, method, ext=''):
        ## 出力ファイルの取得
        return '/'.join([self.dir_data, player + '_' + method + ext])

    def defense(self):
        ## 匿名加工
        self.mkdir_p(self.dir_data)
        for player, method, cmd in self.l_t_player_method_cmd:
            prefix = '{ncat} {tr} | '.format(
                ncat=self.ncat,
                tr=self.cwd + '/' + self.tr)
            suffix = ' | {nsplit} {a0}'.format(
                nsplit=self.nsplit,
                #m0=self.cwd + '/' + self.get_fname(player, method, '.m0'), 
                a0=self.cwd + '/' + self.get_fname(player, method, '.A'),
            )
            cmd = prefix + cmd + suffix
            twd = '/'.join([self.dir_lib, player, method])
            fout = self.get_fname(player, method, '.out')
            ferr = self.get_fname(player, method, '.err')
            self.print_cmd(cmd, twd)
            self.do_shell(cmd, twd, fout, ferr)

if __name__=='__main__':
    file_player = 'player.csv'
    if len(argv) >= 2:
        file_player = argv[1]
    d = Defense(file_player)
    d.defense()
