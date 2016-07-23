import tchisla as t

collection = t.Collection(1)
collection.build(10)
collection.output(None)
print "Complexity is:"
print t.Solution.registry[2016].complexity
