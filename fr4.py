'''#Lists
Lanugages=["Python","C","C++", "Java", 102, 68.1]
#index value 0       1     2      3     4     5
print(Lanugages)
print(Lanugages[5])
print(Lanugages[1:4])
print(Lanugages[2:])
Lanugages.append(80)
print(Lanugages)
Lanugages.insert(4,80)
print(Lanugages)
Lanugages.remove(102)
Lanugages[4]=500
print(Lanugages)
#Tuple
Lanugages=("Python","C","C++", "Java", 102, 68.1)
#index value 0       1     2      3     4     5
print(Lanugages)
print(Lanugages[5])
print(Lanugages[1:4])
print(Lanugages[2:])

Lanugages.remove("HTML")
print(Lanugages)
'''
#For loop
Lanugages=["Python","C","C++", "Java", 102, 68.1]
for i in Lanugages:
    print(i)


x="Hello World"
# 012345678910
for i in x:
    print(i)
for a in range(0,10):
    print(a)
num=int(input("Enter a number: "))
for b in range(1,11):
    print(num,"x", b,"=", num*a)
