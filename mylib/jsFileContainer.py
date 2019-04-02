#coding=utf-8

import mylib.jsFile as jsFile

class JSFileContainer():

    container = None

    def __init__(self, jsfiles: list):
        self.container = jsfiles
    
    def __repr__(self):
        class fakefile():
            output_word = ""
            def write(self, s):
                self.output_word = self.output_word + str(s)
        ff = fakefile()
        print(self.container, file = ff)
        return ff.output_word

    def get_by_name(self, name):
        for i in self.container:
            if i.name == name:
                return i
