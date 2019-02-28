#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.xlsmHub as XH
import mylib.projIni as PJI

class base(CLIS.CLISCMDBASE.base):

    name = "pack"

    def run(self):
        argu = self.get_argu()
        print argu
        xlsm_path = PJI.projIni().get_xlsm_full_path()
        XH.XlsmHub().set_xlsm_path(xlsm_path)
        # XH.XlsmHub().open()
        XH.XlsmHub().input_js_file()
        # XH.XlsmHub().close()