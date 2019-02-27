#coding=utf-8

class JSHub():
    sheet = None
    
    def __init__(self, sheet):
        self.sheet = sheet

    def read_js_file(self, row):
        print self.get_js_name(row)
        print "1 " + self.read_cell(row,2)
        print "2 " + self.read_cell(row,3)
        print "3 " + self.read_cell(row,4)

    def read_cell(self, row, col):
        return str(self.sheet.range((row,col)).value)
    
    def get_js_name(self, row):
        return self.read_cell(row, 1)