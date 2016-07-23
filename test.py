import tchisla as t

collection = t.Collection(6)
collection.build(3)
print '*************'
collection.output(None)
print "Complexity is:"
print t.Solution.registry[27].complexity
