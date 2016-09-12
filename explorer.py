#!/usr/bin/env python

import requests
import json
import sympy
import tchisla as t

digit = 6
depth = 6

cache_limit = 1000000

registry = {}

resp = requests.get("http://www.euclidea.xyz/api/v1/game/numbers/solutions/records?&query={gte:1,lte:" + repr(cache_limit) + "}")
all_records = json.loads(resp.content)['records']
print "loaded {0} records from API".format(len(all_records))

for record in all_records:
  if int(record['digits']) == digit:
    registry[int(record['target'])] = int(record['digits_count'])

collection = t.Collection(digit)
collection.build(depth)
print len(t.Solution.registry)

for target in xrange(1, 1601):
  target_digits = registry[target] - 1
  if target % 10 == 0:
    print target

  for solution1 in collection.iter_solution():
    value1 = solution1.number
    if value1 <= 0:
      continue
    value2 = sympy.Rational(1) * target / value1
    if value2 in t.Solution.registry:
      solution2 = t.Solution.registry[value2]
      if solution1.complexity + solution2.complexity <= target_digits:
        print "\aFound solution (*) for ", target
        print solution1.formatted()
        print solution2.formatted()
        break
    value2 = sympy.Rational(1) * target * value1
    if value2 in t.Solution.registry:
      solution2 = t.Solution.registry[value2]
      if solution1.complexity + solution2.complexity <= target_digits:
        print "\aFound solution (/) for ", target
        print solution1.formatted()
        print solution2.formatted()
        break

    value2 = sympy.Rational(1) * target - value1
    if value2 in t.Solution.registry:
      solution2 = t.Solution.registry[value2]
      if solution1.complexity + solution2.complexity <= target_digits:
        print "\aFound solution (+) for ", target
        print solution1.formatted()
        print solution2.formatted()
        break
