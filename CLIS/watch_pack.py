#coding=utf-8

import CLIS.CLISCMDBASE
import mylib.xlsmHub as XH
import mylib.projIni as PJI
import win32.win32api as win32api
import win32.win32event as win32event
import mylib.path as mypath
import _thread
import time
import CLIS.pack as CLIS_PACK

class base(CLIS.CLISCMDBASE.base):

    name = "watch_pack"
    can_pack = False

    def run(self):
        argu = self.get_argu()
        if argu == "here":
            _thread.start_new_thread(self.file_change, ())
            _thread.start_new_thread(self.wait_for_pack_xlsm, ())
            while(True):
                time.sleep(5)
            return

    def file_change(self):
        handler = win32api.FindFirstChangeNotification(mypath.abs_path(""), True, 0x00000010)
        while(True):
            kee = win32api.FindNextChangeNotification(handler)
            win32event.WaitForSingleObject(handler, -1)
            self.can_pack = True
    
    def wait_for_pack_xlsm(self):
        while(True):
            if(self.can_pack):
                time.sleep(1)
                CLIS_PACK.base().pack_xlsm()
                self.can_pack = False

