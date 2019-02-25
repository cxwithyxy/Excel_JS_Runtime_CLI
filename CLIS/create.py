#coding=utf-8

import CLIS.CLISCMDBASE
import pathlib
import mylib.path
import requests


class base(CLIS.CLISCMDBASE.base):

    name = "create"

    xlsm_download_url = "https://raw.githubusercontent.com/cxwithyxy/Excel_JS_Runtime/master/release/base.xlsm"

    def run(self):
        self.make_path()
        self.down_xlsm()

    def make_path(self):
        mylib.path.mkdir(self.get_argu())
        mylib.path.mkdir(
            mylib.path.join_path(self.get_argu(), "src")
        )

    def down_xlsm(self):
        r = requests.get(self.xlsm_download_url, stream=True)
        f = open(mylib.path.join_path(self.get_argu(), self.get_argu() + ".xlsm"), "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)

