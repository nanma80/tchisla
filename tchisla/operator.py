import math
# from sympy import *


class Operator(object):
  unary = ['sqrt', '!']
  binary = ['+', '-', '*', '/', '^']

  @classmethod
  def apply_unary(cls, operator, input_1):
    def sqrt(input):
      output = math.sqrt(input)
      if output % 1 == 0:
        return int(output)
      else:
        return None

    def factorial(input):
      if input < 30:
        return math.factorial(input)
      else:
        return None

    return {
      'sqrt': sqrt,
      '!': factorial
    }[operator](input_1)

  @classmethod
  def apply_binary(cls, operator, input_1, input_2):
    def add(input_1, input_2):
      return input_1 + input_2

    def subtract(input_1, input_2):
      result = input_1 - input_2
      if result > 0:
        return result
      else:
        return None

    def times(input_1, input_2):
      return input_1 * input_2

    def divide(input_1, input_2):
      if input_2 == 0:
        return None
      if input_1 % input_2 == 0:
        return input_1 / input_2
      else:
        return None

    def power(input_1, input_2):
      if input_2 > 100:
        return None
      result = input_1 ** input_2
      if result < 10 ** 30:
        return result
      else:
        return None

    return {
      '+': add,
      '-': subtract,
      '*': times,
      '/': divide,
      '^': power
    }[operator](input_1, input_2)
