#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.xlsmHub as XH
import mylib.projIni as PJI
import win32.win32api as win32api
import win32.win32event as win32event
import mylib.path as mypath

class base(CLIS.CLISCMDBASE.base):

    name = "watch_pack"

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            self.file_change()
            # xlsm_path = PJI.projIni().get_xlsm_full_path()
            # XH.XlsmHub().set_xlsm_path(xlsm_path)
            # XH.XlsmHub().open()
            # XH.XlsmHub().input_js_file()
            # XH.XlsmHub().close()
            return
    def file_change(self):
        handler = win32api.FindFirstChangeNotification(mypath.abs_path(""), True, 0x00000010)
        print(handler)
        while(True):
            kee = win32api.FindNextChangeNotification(handler)
            win32event.WaitForSingleObject(handler, -1)

