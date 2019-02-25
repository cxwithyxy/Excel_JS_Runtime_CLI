#coding=utf-8

class base():
    
    parser = None
    name = None

    def __init__(self, parser):
        self.parser = parser
        parser.add_argument("-" + self.name)
        
    def get_argu(self):
        argu = vars(self.parser.parse_args())
        return argu[self.name]
    
    def is_match(self):
        if self.get_argu() == None:
            return False
        return True

    def handle_run(self):
        if self.is_match():
            self.run()

    def run(self):
        raise "function \"run\" mast be rewritten"
