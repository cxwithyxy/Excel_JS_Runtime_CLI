#coding=utf-8

import mylib.PythonSingleton.Singleton as SLT

class base(SLT.Singleton):
    
    parser = None
    name = None
    help_str = ""

    def __Singleton_Init__(self, parser = None):
        self.parser = parser
        parser.add_argument("-" + self.name, help = self.help_str)
        
    def get_argu(self):
        argu = vars(self.parser.parse_args())
        return argu[self.name]
    
    def is_match(self):
        if self.get_argu() == None:
            return False
        return True

    def handle_run(self,) -> bool:
        if self.is_match():
            self.run()
            return True
        return False

    def run(self):
        raise "function \"run\" mast be rewritten"
