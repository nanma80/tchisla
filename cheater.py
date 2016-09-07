import requests
import json

target = 6400
digits_count = 6
digit = 7

cache_limit = 1000000

registry = {}

resp = requests.get("http://www.euclidea.xyz/api/v1/game/numbers/solutions/records?&query={gte:1,lte:" + repr(cache_limit) + "}")
all_records = json.loads(resp.content)['records']
print "loaded {0} records from API".format(len(all_records))

for record in all_records:
  if int(record['digits']) == digit:
    registry[int(record['target'])] = int(record['digits_count'])

for plus_1 in xrange(1, cache_limit):
  if plus_1 in registry:
    if registry[plus_1] >= digits_count:
      continue
    plus_2 = abs(target - plus_1)
    if plus_2 in registry:
      if registry[plus_1] + registry[plus_2] <= digits_count:
        print "Found solution (plus) with ", plus_1, registry[plus_1], plus_2, registry[plus_2]
        exit()

for times_1 in xrange(1, target):
  if times_1 in registry:
    if registry[times_1] >= digits_count:
      continue
    if target % times_1 != 0:
      continue
    times_2 = target / times_1
    if times_2 in registry:
      if registry[times_1] + registry[times_2] <= digits_count:
        print "Found solution (times) with ", times_1, registry[times_1], times_2, registry[times_2]
        exit()

for denominator in xrange(1, cache_limit / target):
  if denominator in registry:
    if registry[denominator] >= digits_count:
      continue
    nominator = denominator * target
    if nominator <= cache_limit:
      if nominator in registry:
        if registry[denominator] + registry[nominator] <= digits_count:
          print "Found solution (division) with ", nominator, registry[nominator], denominator, registry[denominator]
          exit()
