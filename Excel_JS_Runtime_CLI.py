#coding=utf-8

import argparse
import CLIS.create
import CLIS.spread

parser = argparse.ArgumentParser()

CLIS.create.base(parser).handle_run()