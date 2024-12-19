a = set() # Empty Set
print(a)

a.add(1)    # Adding elements in set
a.add(1)    # set contain non-repeatable elements
a.add(2)
a.add(3)
a.add(4)
a.add((5,6))
# a.add({3,4})   # lists or dictionary not add in sets
print(a)

# S E T - F U N C T I O N S
print(len(a))

a.remove(3)
# b.remove(10) # throws an error while trying to remove 10 (which is not present in the set)
print(a)

a.pop()       # remove any 1 element from set
print(a)

a.clear()      # empty set remove all element
print(a)