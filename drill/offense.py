#!/usr/bin/env python3
#
# offense.py
#
# [USAGE] python3 offense.py [player.csv]

from sys import argv
from base import Base
from defense import Defense
from publish import Publish

class Offense(Base):
    def __init__(self, file_player):
        self.dir_data = self.dir_out + '/offense'
        self.l_t_player_method_cmd = self.read_l_t_player_method_cmd(file_player, 'offense')
        self.d = Defense(file_player)
        self.p = Publish(file_player)

    def get_fname(self, defense, shield, offense, spear, ext=''):
        ## 出力ファイル名の取得
        tag = '_'.join([defense, shield, offense, spear])
        return '/'.join([self.dir_data, tag + ext])

    def offense(self):
        ## 再識別
        self.mkdir_p(self.dir_data)
        for defense, shield, _ in self.d.l_t_player_method_cmd:
            prefix = '{ncat} {tr} {a1} | '.format(
                ncat=self.ncat,
                tr=self.cwd + '/' + self.tr,
                a1=self.cwd + '/' + self.p.get_fname(defense, shield, '.A1'),
            )
            for offense, spear, cmd in self.l_t_player_method_cmd:
                suffix = ' | {nsplit} {f1}'.format(
                    nsplit=self.nsplit,
                    f1=self.cwd + '/' + self.get_fname(defense, shield, offense, spear, '.F1'))
                cmd = prefix + cmd + suffix
                twd = '/'.join([self.dir_lib, offense, spear])
                fout = self.get_fname(defense, shield, offense, spear, '.out')
                ferr = self.get_fname(defense, shield, offense, spear, '.err')
                self.print_cmd(cmd, twd)
                self.do_shell(cmd, twd, fout, ferr)

if __name__=='__main__':
    file_player = 'player.csv'
    if len(argv) >= 2:
        file_player = argv[1]
    o = Offense(file_player)
    o.offense()
