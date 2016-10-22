#!/usr/bin/env python

import os
import sys

filename, digits = sys.argv

os.system("./refresh_cache.py")
os.system("./range_cheater.py 1 10000 {} {} skip".format(digits, digits))
os.system("./refresh_cache.py")
os.system("./wr_checker.py 1 10000 {} > results/wr_checker_{}.txt".format(digits, digits))
