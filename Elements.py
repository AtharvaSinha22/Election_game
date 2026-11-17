#Adding elements

##'''
##1. append()
##2. extend()
##3. insert()
##
##<name of list>.append(<append>)
##
##'''
##
##L = [4,3,2,1,78]
##print(L)
##L.append(9)
##
##L1 = ["apple", "banana", "cheery"]
##
##L.extend(L1)
##print(L)
##
##L.insert(2,19)
##print(L)
##L = []
##n = int(input("Enter the number of elements in the list: "))
##
##for i in range(n):
##        element = eval(input("Enter element: "))
##        L.append(element)
##print(L)
##
###deleting elements from list

#1.list.remove

#3.list.pop(removes last elements)
#4. del list[index no.]
#5. list.clear

x = [1,2,3,4,5,6]
x.remove(3)
print(x)
x1 = x.pop(2)
print(x)

#x.clear()
#print(x)

del x[0]
print(x)


