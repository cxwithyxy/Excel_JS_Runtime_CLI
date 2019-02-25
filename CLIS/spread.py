#coding=utf-8

import CLIS.CLISCMDBASE

class base(CLIS.CLISCMDBASE.base):

    name = "spread"

    def run(self):
        print self.get_argu()