#coding=utf-8

import argparse
import queue
import sys
import CLIS.create
import CLIS.spread
import CLIS.pack
import CLIS.watch_pack

parser = argparse.ArgumentParser()
myQueue = queue.Queue()

myQueue.put(CLIS.create.base(parser).handle_run)
myQueue.put(CLIS.spread.base(parser).handle_run)
myQueue.put(CLIS.pack.base(parser).handle_run)
myQueue.put(CLIS.watch_pack.base(parser).handle_run)

while not myQueue.empty():
    myQueue.get()()