import os.path
import requests
import json

DEFAULT_CACHE_LIMIT = 1000000000

tmp_dir = 'tmp'
cache_path = tmp_dir + "/records.json"

def get_gs_records():
  registry = {}
  for digits in xrange(1, 10):
    registry[digits] = {'digits': digits}

  gs_records_filename = 'gs_records.txt'

  with open(gs_records_filename, 'r') as f:
    for line in f:
      content = line.strip("\n")
      problem, digits_count = content.split(" ")
      target, digits = problem.split("#")
      target, digits, digits_count = int(target), int(digits), int(digits_count)
      registry[digits][target] = digits_count
  return registry

def load(cache_limit=DEFAULT_CACHE_LIMIT):
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


def get_all(cache_limit=DEFAULT_CACHE_LIMIT, merge_gs_records=True):
  registry = {}
  for digits in xrange(1, 10):
    registry[digits] = {'digits': digits}

  all_records = load(cache_limit)
  gs_records = get_gs_records()

  for record in all_records:
    digits = int(record['digits'])
    target = int(record['target'])
    digits_count = int(record['digits_count'])

    if digits >= 1 and digits <= 9:
      if merge_gs_records and target in gs_records[digits]:
        registry[digits][target] = min(digits_count, gs_records[digits][target])
      else:
        registry[digits][target] = digits_count

  if merge_gs_records:
    for digits in xrange(1, 10):
      for target in gs_records[digits]:
        if target not in registry[digits]:
          registry[digits][target] = gs_records[digits][target]

  inject_repeated_digits(registry)
  return registry


def get(digits, cache_limit=DEFAULT_CACHE_LIMIT):
  return get_all(cache_limit)[digits]
