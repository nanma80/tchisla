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

for final_digit in xrange(final_digit_lower_bound, final_digit_upper_bound + 1):
  records = all_records[final_digit]
  for final_target in xrange(target_lower_bound, target_upper_bound + 1):
    if final_target not in records:
      print "No record for {}#{}".format(final_target, final_digit)
    else:
      final_digits_count = records[final_target]
      print "{}#{} ({})".format(final_target, final_digit, final_digits_count)
      solution = t.cheater.solve(final_target, final_digits_count, records)
      print solution
      if solution is not None:
        if final_target not in api_records[final_digit] or api_records[final_digit][final_target] > final_digits_count:
          t.records.submit(final_target, final_digit, final_digits_count, solution)

    print

sorted_unsolved_problems = sorted(t.cheater.unsolved_problems.keys(), key=lambda x: (x[1], x[0]))

print "Unsolved:"

for unsolved_problem in sorted_unsolved_problems:
  print "{}#{} = {}".format(unsolved_problem[0], unsolved_problem[1], t.cheater.unsolved_problems[unsolved_problem])
