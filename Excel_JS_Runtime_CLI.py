#coding=utf-8

import argparse
import Queue
import sys
import CLIS.create
import CLIS.spread
import CLIS.pack

# 设定python默认字符集
reload(sys)
sys.setdefaultencoding( "gbk" )


parser = argparse.ArgumentParser()
queue = Queue.Queue()

queue.put(CLIS.create.base(parser).handle_run)
queue.put(CLIS.spread.base(parser).handle_run)
queue.put(CLIS.pack.base(parser).handle_run)

while not queue.empty():
    queue.get()()