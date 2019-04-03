#coding=utf-8

import mylib.jsFile as jsFile
from multiprocessing.pool import ThreadPool as Pool

class JSFileContainer():

    container = None
    filter_jsfile_names = []

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

    def add_filter_js_names(self, names: list):
        self.filter_jsfile_names.extend(names)

    def filter_out_JSFileContainer(self):
        prs = []
        def pool_do(now_jsFile: jsFile):
            is_match = False
            for i in self.filter_jsfile_names:
                if i == now_jsFile.name:
                    is_match = True
            if not is_match:
                prs.append(now_jsFile)
        pool = Pool()
        pool.map(pool_do, self.container)
        pool.close()
        return JSFileContainer(prs)
    
    def each_do(self, callback):
        for i in self.container:
            callback(i)