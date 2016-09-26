import os.path
import requests
import json

DEFAULT_CACHE_LIMIT = 1000000000


def load(cache_limit=DEFAULT_CACHE_LIMIT):
  tmp_dir = 'tmp'
  cache_path = tmp_dir + "/records.json"

  if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

  read_data = None
  if os.path.exists(cache_path):
    print "Loading records from " + cache_path
    with open(cache_path, 'r') as f:
      read_data = f.read()
  else:
    print "Loading records from API ..."
    resp = requests.get("http://www.euclidea.xyz/api/v1/game/numbers/solutions/records?&query={gte:1,lte:" + repr(cache_limit) + "}")
    read_data = resp.content
    print "Caching records ..."
    with open(cache_path, 'w') as f:
      f.write(read_data)

  all_records = json.loads(read_data)['records']
  print "Loaded {0} records".format(len(all_records))
  return all_records


def inject_repeated_digits(registry):
  for digits in registry:
    for repeat_count in xrange(1, 10):
      number = digits * (10 ** repeat_count - 1) / 9
      if number not in registry[digits]:
        registry[digits][number] = repeat_count


def get_all(cache_limit=DEFAULT_CACHE_LIMIT):
  registry = {}
  for digits in xrange(1, 10):
    registry[digits] = {'digits': digits}

  all_records = load(cache_limit)

  for record in all_records:
    digits = int(record['digits'])
    target = int(record['target'])
    digits_count = int(record['digits_count'])
    if digits >= 1 and digits <= 9:
      registry[digits][target] = digits_count

  inject_repeated_digits(registry)
  return registry


def get(digits, cache_limit=DEFAULT_CACHE_LIMIT):
  return get_all(cache_limit)[digits]
