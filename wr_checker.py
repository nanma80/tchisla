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


all_records = t.records.get_all()
api_records = t.records.get_api_records()

for digits in xrange(1, 10):
  print "Processing #{}".format(digits)

  for target in xrange(check_lower_limit, check_upper_limit + 1):
    sub_records = api_records[digits]
    full_records =all_records[digits]
    if target not in sub_records:
      print "No API record for {}#{}".format(target, digits)
      t.cheater.solve(target, full_records[target], full_records)
      print
    # else:
    #   t.cheater.solve(target, sub_records[target] - 1, sub_records, suppress_failure=True)

sorted_unsolved_problems = sorted(t.cheater.unsolved_problems.keys(), key=lambda x: (x[1], x[0]))

print "Unsolved:"

for unsolved_problem in sorted_unsolved_problems:
  print "{}#{} = {}".format(unsolved_problem[0], unsolved_problem[1], t.cheater.unsolved_problems[unsolved_problem])
