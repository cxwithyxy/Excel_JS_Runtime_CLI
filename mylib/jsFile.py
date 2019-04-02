#coding=utf-8

import math

class JSFile():

    name = None
    
    base_path = None
    
    code = None

    def set_base_path(self, path):
        self.base_path = path

    def save(self, base_path = None):
        if base_path != None :
            self.set_base_path(base_path)
        temp_f = open(self.base_path + "/" + self.name, mode = 'wb')
        temp_f.write(self.code.encode("utf-8"))
        temp_f.close()
    
    def decode_str_into_code(self, str):
        self.code = str.replace(u"_等于号_", "=")

    def encode_code(self):
        return self.code.replace("=", u"_等于号_")

    def load_js_file(self, js_file_path):
        self.name = js_file_path
        temp_f = open(js_file_path, mode = "rb")
        self.code = temp_f.read().decode("utf-8")
        temp_f.close()

    def __repr__(self):
        return self.name + " -- " + str(len(self.code))

    def rename_by_src_path(self, src_path):
        self.name = self.name.replace(src_path, "")

    def write_in_sheet(self, sheet, y, need_encode = False):
        file_seek_offset = 32000
        code_encoded = self.code if(not need_encode) else self.encode_code()
        loop_count = len(code_encoded) / file_seek_offset
        loop_count = math.ceil(loop_count)
        for i in range(loop_count):
            temp = code_encoded[i * file_seek_offset : (i + 1) * file_seek_offset]
            sheet.range((y, i + 2)).value = temp
        sheet.range((y, 1)).value = self.name

