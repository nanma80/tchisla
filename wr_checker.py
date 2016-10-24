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

unsolved_count = 0
unknown_count = 0

for digits in xrange(final_digit_lower_bound, final_digit_upper_bound + 1):
  print "Processing #{}".format(digits)

  for target in xrange(target_lower_bound, target_upper_bound + 1):
    sub_records = api_records[digits]
    full_records =all_records[digits]
    if target not in sub_records:
      print "No API record for {}#{}".format(target, digits)
      t.cheater.solve(target, full_records[target], full_records, fail_fast=True)
      print
      unknown_count += 1
    elif sub_records[target] > full_records[target]:
      print "{}#{}: API: {}; GS: {}".format(target, digits, sub_records[target], full_records[target])
      t.cheater.solve(target, full_records[target], full_records, fail_fast=True)
      print
      unknown_count += 1


sorted_unsolved_problems = sorted(t.cheater.unsolved_problems.keys(), key=lambda x: (x[1], x[0]))
unsolved_count = len(sorted_unsolved_problems)

aggregated_unsolved_problems = {}
for unsolved_problem in sorted_unsolved_problems:
  target = unsolved_problem[0]
  digits = unsolved_problem[1]
  count = t.cheater.unsolved_problems[unsolved_problem]

  if (digits, count) in aggregated_unsolved_problems:
    aggregated_unsolved_problems[(digits, count)].append(target)
  else:
    aggregated_unsolved_problems[(digits, count)] = [target]

print "{} problems need to be improved. {} need to be solved. The rest can be easily deduced.".format(unknown_count, unsolved_count, unknown_count - unsolved_count)
print "{} problem to be solved:".format(unsolved_count)
for (digits, count) in sorted(aggregated_unsolved_problems.keys()):
  targets = aggregated_unsolved_problems[(digits, count)]
  targets_string = [str(target) for target in targets]

  print "[{}]#{} -d {}".format(','.join(targets_string), digits, count)


