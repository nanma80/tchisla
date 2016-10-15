#!/usr/bin/env python

import sys
import tchisla as t

if len(sys.argv) == 2:
  filename, target_lower_bound_string = sys.argv
  target_upper_bound_string = target_lower_bound_string
  digit_lower_bound_string = '1'
  digit_upper_bound_string = '9'
elif len(sys.argv) == 3:
  filename, target_lower_bound_string, target_upper_bound_string = sys.argv
  digit_lower_bound_string = '1'
  digit_upper_bound_string = '9'
elif len(sys.argv) == 4:
  filename, target_lower_bound_string, target_upper_bound_string, digit_lower_bound_string = sys.argv
  digit_upper_bound_string = digit_lower_bound_string
elif len(sys.argv) == 5:
  filename, target_lower_bound_string, target_upper_bound_string, digit_lower_bound_string, digit_upper_bound_string = sys.argv

target_lower_bound = int(target_lower_bound_string)
target_upper_bound = int(target_upper_bound_string)
final_digit_lower_bound = int(digit_lower_bound_string)
final_digit_upper_bound = int(digit_upper_bound_string)

all_records = t.records.get_all()
api_records = t.records.get_api_records()

for digits in xrange(final_digit_lower_bound, final_digit_upper_bound + 1):
  print "Processing #{}".format(digits)

  for target in xrange(target_lower_bound, target_upper_bound + 1):
    sub_records = api_records[digits]
    full_records =all_records[digits]
    if target not in sub_records:
      print "No API record for {}#{}".format(target, digits)
      t.cheater.solve(target, full_records[target], full_records)
      print

sorted_unsolved_problems = sorted(list(t.cheater.unsolved_problems.iteritems()), key=lambda x:(x[0][1],x[1],x[0][0]))

print "Unsolved:"

for unsolved_problem in sorted_unsolved_problems:
  print "{}#{} = {}".format(unsolved_problem[0][0], unsolved_problem[0][1], unsolved_problem[1])
