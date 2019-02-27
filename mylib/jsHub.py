#coding=utf-8

import jsFile

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
        js_file.code = reading_str
        return js_file

    def read_cell(self, row, col):
        return str(self.sheet.range((row,col)).value)
    
    def get_js_name(self, row):
        return self.read_cell(row, 1)