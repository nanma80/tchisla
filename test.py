import tchisla as t

collection = t.Collection(4)
collection.build(4)
collection.output(None)
print "Complexity is:"
print t.Solution.registry[4].complexity
