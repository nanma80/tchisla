#!/usr/bin/env python

import sys
import tchisla as t

if len(sys.argv) == 2:
  filename, check_limit_string = sys.argv
  check_upper_limit = int(check_limit_string)
  check_lower_limit = 1
if len(sys.argv) == 3:
  filename, check_lower_limit_string, check_limit_string = sys.argv
  check_upper_limit = int(check_limit_string)
  check_lower_limit = int(check_lower_limit_string)


gs_records = t.records.get_gs_records()
api_records = t.records.get_all(merge_gs_records=False)

for digits in xrange(1, 10):
  print "#{}:".format(digits)

  for target in xrange(check_lower_limit, check_upper_limit + 1):
    api_sub_records = api_records[digits]
    gs_sub_records = gs_records[digits]

    if target not in gs_sub_records:
      print "No GS record for {}#{}".format(target, digits)
    elif target not in api_sub_records:
      # API records are known to be incomplete
      pass
    else:
      if api_sub_records[target] != gs_sub_records[target]:
        print "{}#{}: API: {}; GS: {}".format(target, digits, api_sub_records[target], gs_sub_records[target])
  print
