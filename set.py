# is a collection of unnordered items
# each element in a set must be unique or immuteable but set is muteable
# string and tuplles are store in set 
# list and dictionaries are not store in set
# ignore duplicate values
"""
set={1,2,3,4}
print(set)
print(type(set))
print(len(set))

# empty set
emp={}               # error because it create empty dictionary
emp=set()            # correct 


# sets method

# add(add a new element)
set=set()
set.add(1)
set.add(2)
set.add(3)
print(set)

# remove
set.remove(2)
print(set)

# clear(empties the set)
set.clear()
print(len(set))

# pop( removes a random value from set)
set={1,2,3,4}
print(set.pop())

# union
set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))


# intersection
set1={1,2,3}
set2={3,4,5,6}
print(set1.intersection(set2))
"""