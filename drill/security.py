#!/usr/bin/env python3
#
# security.py
#
# [USAGE] python3 security.py [player.csv]
# ruby ncat.rb p.csv q.csv | ruby sec-aprf.rb | ruby nsplit.rb sec.txt

from sys import argv
from base import Base
from defense import Defense
from offense import Offense

class Security(Base):
    def __init__(self, file_player):
        self.dir_data = self.dir_out + '/security'
        self.l_t_player_method_cmd = self.read_l_t_player_method_cmd(file_player, 'security')
        self.d = Defense(file_player)
        self.o = Offense(file_player)

    def get_fname(self, defense, shield, offense, spear, judge, metric, ext=''):
        ## 出力ファイル名の取得
        tag = '_'.join([defense, shield, offense, spear, judge, metric])
        return '/'.join([self.dir_data, tag + ext])

    def security(self):
        ## 安全性評価
        self.mkdir_p(self.dir_data)
        for defense, shield, _ in self.d.l_t_player_method_cmd:
            for offense, spear, _ in self.o.l_t_player_method_cmd:
                prefix = '{ncat} {r_csv} {tr} {a0} {f1} | '.format(
                    ncat=self.ncat,
                    r_csv=self.cwd + '/' + self.r_csv,
                    tr=self.cwd + '/' + self.tr,
                    a0=self.cwd + '/' + self.d.get_fname(defense, shield, '.A'),
                    f1=self.cwd + '/' + self.o.get_fname(defense, shield, offense, spear, '.F1'),
                )
                for judge, metric, cmd in self.l_t_player_method_cmd:
                    suffix = ' | {nsplit} {sec}'.format(
                        nsplit=self.nsplit,
                        sec=self.cwd + '/' + self.get_fname(defense, shield, offense, spear, judge, metric, '.S'))
                    cmd = prefix + cmd + suffix
                    twd = '/'.join([self.dir_lib, judge, metric])
                    fout = self.get_fname(defense, shield, offense, spear, judge, metric, '.out')
                    ferr = self.get_fname(defense, shield, offense, spear, judge, metric, '.err')
                    self.print_cmd(cmd, twd)
                    self.do_shell(cmd, twd, fout, ferr)

if __name__=='__main__':
    file_player = 'player.csv'
    if len(argv) >= 2:
        file_player = argv[1]
    s = Security(file_player)
    s.security()
