#coding=utf-8

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
        # print self.code
        # print js_file_path

    def rename_by_src_path(self, src_path):
        self.name = self.name.replace(src_path, "")

