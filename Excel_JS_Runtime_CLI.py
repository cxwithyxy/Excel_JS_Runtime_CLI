#coding=utf-8

import argparse
import importlib

# parser = argparse.ArgumentParser()
# parser.add_argument("-create")
# args = parser.parse_args()
# print args
a=importlib.import_module("CLIS.a")
b=importlib.import_module("CLIS.b")


print a.bb
print b.bb