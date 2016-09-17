#!/usr/bin/env python

import sys
import tchisla as t

filename, check_limit_string = sys.argv
check_limit = int(check_limit_string)

all_records = t.records.get_all()
for digits in xrange(1, 10):
  print "Processing #{}".format(digits)

  for target in xrange(1, check_limit + 1):
    sub_records = all_records[digits]
    if target not in sub_records:
      print "No record for {}#{}".format(target, digits)
    else:
      t.cheater.solve(target, sub_records[target] - 1, sub_records)
