#!/usr/bin/env python3
#
# utility.py
#
# [USAGE] python3 utility.py [player.csv]

from sys import argv
from base import Base
from defense import Defense

class Utility(Base):
    def __init__(self, file_player):
        self.dir_data = self.dir_out + '/utility'
        self.l_t_player_method_cmd = self.read_l_t_player_method_cmd(file_player, 'utility')
        self.d = Defense(file_player)

    def get_fname(self, defense, shield, offense, spear, ext=''):
        ## 出力ファイル名の取得
        tag = '_'.join([defense, shield, offense, spear])
        return '/'.join([self.dir_data, tag + ext])
    
    def utility(self):
        ## 有用性評価
        self.mkdir_p(self.dir_data)
        for defense, shield, cmd in self.d.l_t_player_method_cmd:
            prefix = '{ncat} {tr} {a0} | '.format(
                ncat=self.ncat,
                tr=self.cwd + '/' + self.tr,
                a0=self.cwd + '/' + self.d.get_fname(defense, shield, '.A'),
            )
            for judge, metric, cmd in self.l_t_player_method_cmd:
                suffix = ' | {nsplit} {ut}'.format(
                    nsplit=self.nsplit,
                    ut=self.cwd + '/' + self.get_fname(defense, shield, judge, metric, '.U'))
                cmd = prefix + cmd + suffix
                twd = '/'.join([self.dir_lib, judge, metric])
                fout = self.get_fname(defense, shield, judge, metric, '.out')
                ferr = self.get_fname(defense, shield, judge, metric, '.err')
                self.print_cmd(cmd, twd)
                self.do_shell(cmd, twd, fout, ferr)

if __name__=='__main__':
    file_player = 'player.csv'
    if len(argv) >= 2:
        file_player = argv[1]
    u = Utility(file_player)
    u.utility()
