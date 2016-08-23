import sys
import tchisla as t

def main():
  filename, base, limit, power_limit = sys.argv
  t.Operator.power_limit = int(power_limit)
  collection = t.Collection(int(base))
  collection.build(int(limit))
  collection.output(None)

if __name__ == '__main__':
  main()
