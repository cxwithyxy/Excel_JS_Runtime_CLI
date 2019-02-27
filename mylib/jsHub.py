#coding=utf-8

class JSHub():
    sheet = None
    
    def __init__(self, sheet):
        self.sheet = sheet

    def read_js_file(self, row):
        print self.get_js_name(row)
        count = 2
        reading_str = ""
        while True:
            temp = self.read_cell(row,count)
            if temp == "None":
                break
            count += 1
            reading_str += temp
        print reading_str
        return 111

    def read_cell(self, row, col):
        return str(self.sheet.range((row,col)).value)
    
    def get_js_name(self, row):
        return self.read_cell(row, 1)