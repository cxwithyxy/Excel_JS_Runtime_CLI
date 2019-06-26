#coding=utf-8

import CLIS.CLISCMDBASE
import pathlib
import mylib.path
import requests
import mylib.projIni as PJI
import CLIS.spread as spread


class base(CLIS.CLISCMDBASE.base):

    name = "create"

    xlsm_download_url = "https://raw.githubusercontent.com/cxwithyxy/Excel_JS_Runtime/master/release/base.xlsm"

    def run(self):
        self.make_path(self.get_argu())
        self.down_xlsm()
        self.make_ini_file(self.get_argu())
        self.spread_xlsm(self.get_argu())

    def make_path(self, proj_name):
        mylib.path.mkdir(proj_name)
        mylib.path.mkdir(
            mylib.path.join_path(proj_name, "src")
        )

    def down_xlsm(self):
        r = requests.get(self.xlsm_download_url, stream=True)
        f = open(mylib.path.join_path(self.get_argu(), self.get_argu() + ".xlsm"), "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)

    def make_ini_file(self, proj_name):
        PJI.projIni().set_base_path(proj_name + "/")
        PJI.projIni().init_config_file(proj_name)

    def spread_xlsm(self, proj_name):
        spread.base().spread_xlsm(
            str(mylib.path.join_path(proj_name, proj_name + ".xlsm"))
        )
