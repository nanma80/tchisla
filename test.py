import tchisla as t

collection = t.Collection(6)
collection.build(5)
collection.output(None)
print "Complexity is:"
print t.Solution.registry[4].complexity
