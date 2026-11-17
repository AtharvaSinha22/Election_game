# Tuples

t = ()
print(type(t))

t = (1,1,1,1, False,[1,2,3],34.2)

print(t[0])
print(t[-1])
print(t[0:3])

print(t[::-1])#reverse

'''t[0] = 11''' #Type error immutable
#allows duplicates
t1 = (1,2,3)
t2 = (4,5,6)
print(t1+t2)


print(t1*3)
for i in t1:
    print(i*3)


t1 = list(t1)
t1.append(4)
t1 = tuple(t1)
print(t1)

t.count(1)

t.index(1)
