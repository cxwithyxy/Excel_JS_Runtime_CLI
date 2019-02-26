#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.projIni as PJI

class base(CLIS.CLISCMDBASE.base):

    name = "spread"

    def run(self):
        print self.get_argu()
        print PJI.projIni().get_xlsm_full_path()