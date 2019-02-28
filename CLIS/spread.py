#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.projIni as PJI
import mylib.xlsmHub as XH

class base(CLIS.CLISCMDBASE.base):

    name = "spread"

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            self.spread_here()
        

    def spread_here(self):
        xlsm_path = PJI.projIni().get_xlsm_full_path()
        XH.XlsmHub().set_xlsm_path(xlsm_path)
        XH.XlsmHub().open()
        XH.XlsmHub().output_js_file()