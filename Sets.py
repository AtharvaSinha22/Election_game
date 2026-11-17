;pppp##unindexed
##unordered
##does not allow duplicates
##partially mutable

s = set()
print(type(s))

s1 = {1,2,3,5,6,7,8}
print(s1)


s2 = {4,3,2,1}
print(s2)


for i in s1:
   print(s1)
#Add
s1.add(0)

s1.update("a")
s1.update(s2)
print(s1)

#Delete

s1.remove(3)
s1.discard(48)
s1.pop()

#del s1  Deletes entier set
print(s1)

#union
#intersection
#difference
#symetric difference


s1.union(s2)
print(s1)
s1.intersection(s2)
print(s1)
s2.difference(s1)
print(s2)
s2.symmetric_difference(s1)
print(s2)

s3 = {1,2,3}
s1.issuperset(s3)

s3.issubset(s1)
s4 = {13,15,17}
s3.isdisjoint(s4)
            
