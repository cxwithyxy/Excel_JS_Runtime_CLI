#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.xlsmHub as XH
import mylib.projIni as PJI

class base(CLIS.CLISCMDBASE.base):

    name = "pack"

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            self.pack_xlsm()
            return

    def pack_xlsm(self):
        xlsm_path = PJI.projIni().get_xlsm_full_path()
        XH.XlsmHub().set_xlsm_path(xlsm_path)
        XH.XlsmHub().open()
        XH.XlsmHub().input_js_file()
        XH.XlsmHub().flash_sheet()
        # XH.XlsmHub().close()
