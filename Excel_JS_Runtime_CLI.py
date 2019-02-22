#coding=utf-8

import argparse
import CLIS.create
import CLIS.spread

parser = argparse.ArgumentParser()

CLIS.create.handle_CLI(parser)()
CLIS.spread.handle_CLI(parser)

print parser.parse_args()