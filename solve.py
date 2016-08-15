import sys
import tchisla as t

def main():
  filename, base, limit = sys.argv
  collection = t.Collection(int(base))
  collection.build(int(limit))
  print 'output:'
  collection.output(None)

if __name__ == '__main__':
  main()
