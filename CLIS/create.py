#coding=utf-8

import CLIS.CLISCMDBASE

class base(CLIS.CLISCMDBASE.base):

    name = "create"

    def run(self):
        print self.get_argu()
