#coding=utf-8

the_parser = None

def run():
    # if the_parser.parse_args().get("create"):
    argu = vars(the_parser.parse_args())
    print argu[__name__.split(".").pop()]
    pass

def handle_CLI(parser):
    global the_parser
    the_parser = parser
    the_parser.add_argument("-create")
    return run
    pass