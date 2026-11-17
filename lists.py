#Lists

l = []
print(type(l))



L1 = [1,17,10,33.4]
print(L1)

#Characteristics

#Indexed
#ordered(order of lists)
#mutable(changeable)
#Duplicates allowed (two or more of the same int, float, string, etc could be in a lists)
print(L1[0])
print(L1[-1])

L1[0] = 11
print(L1)

print(len(L1))

print(max(L1))  
print(min(L1))
print(sum(L1))

#SLICING
print(L1[0:3])
print(L1[::-1])

#for i in L1:
#    print(i)
for i in range(len(L1)):
    print(L1[i])
