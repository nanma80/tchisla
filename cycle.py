#!/usr/bin/env python

import os

os.system("./refresh_cache.py")
os.system("./range_cheater.py 1 10000 1 9 skip")
os.system("./refresh_cache.py")
os.system("./wr_checker.py 1 10000 1 9 > results/wr_checker.txt")
