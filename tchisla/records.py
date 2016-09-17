import requests
import json

DEFAULT_CACHE_LIMIT = 1000000000

def get_all(cache_limit=DEFAULT_CACHE_LIMIT):
  registry = {}
  for digits in xrange(1, 10):
    registry[digits] = {}
  print "Loading records from API ..."
  resp = requests.get("http://www.euclidea.xyz/api/v1/game/numbers/solutions/records?&query={gte:1,lte:" + repr(cache_limit) + "}")
  all_records = json.loads(resp.content)['records']
  print "Loaded {0} records from API".format(len(all_records))

  for record in all_records:
    digits = int(record['digits'])
    target = int(record['target'])
    digits_count = int(record['digits_count'])
    if digits >= 1 and digits <= 9:
      registry[digits][target] = digits_count
  return registry


def get(digits, cache_limit=DEFAULT_CACHE_LIMIT):
  return get_all(cache_limit)[digits]
