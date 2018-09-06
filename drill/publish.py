#!/usr/bin/env python3
#
# offense.py
#
# [USAGE] python3 offense.py [player.csv]

from sys import argv
from base import Base
from defense import Defense

class Publish(Base):
    def __init__(self, file_player):
        self.dir_data = self.dir_out + '/publish'
        self.l_t_player_method_cmd = self.read_l_t_player_method_cmd(file_player, 'publish')
        self.d = Defense(file_player)

    def get_fname(self, defense, shield, ext=''):
        ## 出力ファイル名の取得
        tag = '_'.join([defense, shield])
        return '/'.join([self.dir_data, tag + ext])

    def publish(self):
        ## convert anonymized data to SHUFFLED anonymized data
        self.mkdir_p(self.dir_data)
        for defense, shield, _ in self.d.l_t_player_method_cmd:
            prefix = '{ncat} {a0} | '.format(
                ncat=self.ncat,
                a0=self.cwd + '/' + self.d.get_fname(defense, shield, '.A'),
            )
            for publish, pmethod, cmd in self.l_t_player_method_cmd:
                suffix = ' | {nsplit} {a1}'.format(
                    nsplit=self.nsplit,
                    a1=self.cwd + '/' + self.get_fname(defense, shield, '.A1'))
                cmd = prefix + cmd + suffix
                twd = '/'.join([self.dir_lib, publish, pmethod])
                self.print_cmd(cmd, twd)
                self.do_shell(cmd, twd, 'tmp.out', 'tmp.err')

if __name__=='__main__':
    file_player = 'player.csv'
    if len(argv) >= 2:
        file_player = argv[1]
    p = Publish(file_player)
    p.publish()
