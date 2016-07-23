from generation import *


class Collection():
  """Holds all solutions for all numbers with the same base"""
  def __init__(self, base):
    self.base = base

  def build(self, generation_limit=4):
    for generation_index in xrange(1, generation_limit):
      print "{}/{}".format(generation_index, generation_limit - 1)
      generation = Generation(generation_index, self.base)
      generation.build()

  def output(self, number_limit=100):
    sorted_keys = sorted(Solution.registry.keys())
    for key in sorted_keys:
      if number_limit is None or key <= number_limit:
        solution = Solution.registry[key]
        print solution.formatted()
