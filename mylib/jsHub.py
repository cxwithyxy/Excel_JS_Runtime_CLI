#coding=utf-8

import jsFile
import mylib.path
from multiprocessing.pool import ThreadPool as Pool

class JSHub():

    sheet = None
    
    def __init__(self, sheet):
        self.sheet = sheet

    def read_js_file(self, row):
        name = self.get_js_name(row)
        if name == "None":
            return False
        count = 2
        reading_str = ""
        while True:
            temp = self.read_cell(row,count)
            if temp == "None":
                break
            count += 1
            reading_str += temp
        js_file = jsFile.JSFile()
        js_file.name = name
        js_file.decode_str_into_code(reading_str)
        return js_file

    def read_cell(self, row, col):
        return str(self.sheet.range((row,col)).value)
    
    def get_js_name(self, row):
        return self.read_cell(row, 1)

    def read_js_file_from_src(self, src_path):
        jsss =  mylib.path.get_all_js_path_from_src(src_path)
        def pool_do(ipath):
            js_file = jsFile.JSFile()
            js_file.load_js_file(ipath)
            js_file.rename_by_src_path(src_path + "\\")
            return js_file
        pool = Pool()
        prs = pool.map(pool_do, jsss)
        pool.close()
        return prs

    def write_js_file_in_sheet(self, src_path):
        jsfiles = self.read_js_file_from_src(src_path)
        writting_order = [
            "BASE_INIT.js",
            "CXAMD.js"
            # "UpdataJSFiles.js",
            # "before_RequireJS.min.js",
            # "CX_RequireJS.min.js"
        ]
        print jsfiles
        self.sheet.clear()
        jsfiles[2].write_in_sheet(self.sheet, 1, True)