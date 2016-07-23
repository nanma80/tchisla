# import math
import sympy

class Operator(object):
  unary = ['sqrt', '!', '-']
  binary = ['+', '-', '*', '/', '^']

  @classmethod
  def apply_unary(cls, operator, input_1):
    def sqrt(input):
      if input <= 0:
        return None
      output = sympy.sqrt(input)
      if output % 1 == 0:
        return int(output)
      else:
        return None

    def factorial(input):
      if input < 30 and input > 0 and input % 1 == 0:
        return sympy.factorial(input)
      else:
        return None

    def negate(input):
      return (-input)

    return {
      'sqrt': sqrt,
      '!': factorial,
      '-': negate
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
      return sympy.Rational(input_1, input_2)

    def power(input_1, input_2):
      if input_2 > 30 or input_2 < -30:
        return None
      if input_1 <= 0:
        return None
      result = input_1 ** input_2
      if result < 10 ** 30 and result > 0.1 ** 30:
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
