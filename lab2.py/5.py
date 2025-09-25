myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# copy()	Returns a shallow copy
# difference()	Returns a new frozenset with the difference
# intersection()	&	Returns a new frozenset with the intersection
# isdisjoint()	Returns whether two frozensets have an intersection
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another
# symmetric_difference()	^	Returns a new frozenset with the symmetric differences
# union()	|	Returns a new frozenset containing the union



# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
# <	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
# >	Returns True if all items of another, smaller set is present in this set
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others


