set={10,20,30,40,50,60,70,80,90,100}
print(set)
print(type(set))
#membership operator
print(30 in set)
#add method
set.add(110)
print(set)
#update-adds the given elements
set2={120,130,140,150}
set.update(set2)
print(set)
#remove-removes the given element
set.remove(10)
print(set)
#discard-removes the specific item
set.discard(100)
print(set)
#pop-remove and return an arbitary item
set.pop()
print(set)
#clear-removes all items from the set
set.clear()
print(set)
#union(|)-returns all the unique items for both sets
set1={1,2,3}
set2={3,4,5}
print(set1|set2)
#intersection(&)-returns all the common elements
set1={1,2,3}
set2={2,3,4}
print(set1&set2)
#difference(-)-returns a set containing that are only in first set but not in the second set
print(set1-set2)
#symmetric difference(^)-returns a set containing items that are in either set but not both
print(set1^set2)