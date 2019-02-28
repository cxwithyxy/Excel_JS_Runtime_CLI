#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.projIni as PJI
import mylib.xlsmHub as XH
import create

class base(CLIS.CLISCMDBASE.base):

    name = "spread"

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            self.spread_here()
            return
        self.spread_exist_xlsm(argu)

    def spread_exist_xlsm(self, xlsm_path):
        
        create.base().make_path(xlsm_path)
        # create.base().down_xlsm(xlsm_path)
        create.base().make_ini_file(xlsm_path)
        # create.base().spread_xlsm(xlsm_path)

    def spread_here(self):
        xlsm_path = PJI.projIni().get_xlsm_full_path()
        self.spread_xlsm(xlsm_path)

    def spread_xlsm(self, xlsm_path):
        XH.XlsmHub().set_xlsm_path(xlsm_path)
        XH.XlsmHub().open()
        XH.XlsmHub().output_js_file()