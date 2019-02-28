#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.projIni as PJI
import mylib.xlsmHub as XH
import create
import mylib.path

class base(CLIS.CLISCMDBASE.base):

    name = "spread"

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            self.spread_here()
            return
        self.spread_exist_xlsm(argu)

    def spread_exist_xlsm(self, xlsm_path):
        if not mylib.path.is_exist(xlsm_path):
            print xlsm_path + u" 文件不存在"
            exit()
        proj_name = mylib.path.get_file_name_without_suffixs(xlsm_path)
        create.base().make_path(proj_name)
        mylib.path.move_path(xlsm_path, proj_name + "/" + xlsm_path)
        create.base().make_ini_file(proj_name)
        create.base().spread_xlsm(proj_name)

    def spread_here(self):
        xlsm_path = PJI.projIni().get_xlsm_full_path()
        self.spread_xlsm(xlsm_path)

    def spread_xlsm(self, xlsm_path):
        XH.XlsmHub().set_xlsm_path(xlsm_path)
        XH.XlsmHub().open()
        XH.XlsmHub().output_js_file()
        XH.XlsmHub().close()