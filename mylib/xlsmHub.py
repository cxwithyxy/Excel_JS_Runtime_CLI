#coding=utf-8

import mylib.PythonSingleton.Singleton as SLT
import xlwings as xw
import mylib.path
import jsHub

class XlsmHub(SLT.Singleton):

    xlsm_obj = None
    xlsm_path = None
    js_hub = None

    def __Singleton_Init__(self):
        pass

    def set_xlsm_path(self, xlsm_path):
        self.xlsm_path = xlsm_path

    def close(self):
        self.xlsm_obj.app.kill()

    def open(self):
        self.xlsm_obj = xw.Book(self.xlsm_path)
        self.js_hub = jsHub.JSHub(self.javascript_saving_sheet())

    def javascript_saving_sheet(self):
        return self.xlsm_obj.sheets["BASE_CODE_LIB"]
    
    def output_js_file(self):
        js_saving_path = mylib.path.get_js_saving_path_base_on_xlsm(self.xlsm_path)
        count = 1
        while True:
            temp_file = self.js_hub.read_js_file(count)
            if temp_file == False:
                break
            count += 1
            temp_file.save(js_saving_path)
        pass