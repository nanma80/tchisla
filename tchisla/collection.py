import sympy
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

  def output(self, number_limit=None):
    for solution in self.iter_solution(number_limit):
      print solution.formatted()

  def iter_solution(self, number_limit=None):
    sorted_keys = sorted(Solution.registry.keys(), key=lambda x: sympy.N(x))
    for key in sorted_keys:
      if number_limit is None or key <= number_limit:
        yield Solution.registry[key]
