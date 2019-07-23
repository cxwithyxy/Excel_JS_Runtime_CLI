#coding=utf-8

import argparse
import queue
import sys
import CLIS.create
import CLIS.spread
import CLIS.pack
import CLIS.watch_pack

parser = argparse.ArgumentParser()
parser.description = "===== Excel_JS_Runtime_CLI v1.201907231125 ====="
parser.epilog ="* MORE INFO: https://github.com/cxwithyxy/Excel_JS_Runtime_CLI"
myQueue = queue.Queue()

myQueue.put(CLIS.create.base(parser).handle_run)
myQueue.put(CLIS.spread.base(parser).handle_run)
myQueue.put(CLIS.pack.base(parser).handle_run)
myQueue.put(CLIS.watch_pack.base(parser).handle_run)

has_match_cmd = False
while not myQueue.empty():
    if(myQueue.get()()):
        has_match_cmd = True
        break

if(not has_match_cmd):
    parser.print_help()