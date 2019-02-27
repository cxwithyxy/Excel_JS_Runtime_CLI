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

