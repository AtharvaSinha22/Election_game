#1.Write a Python program that takes a list of numbers and returns a new list with only the even numbers from the original list

L = []
n = int(input("Enter number of elements : "))
for i in range(n):
    e = int(input("Enter the numbers of your list: "))
if( e % 2 == 0):
 L.append(e)
 print(L)

#2 Write a Python program that takes two lists as input and merges them into a single list, alternating elements from each list.

L = []
n = int(input("Enter number of elements : "))
for i in range(n):
    e = eval(input("Enter the elements of your list: "))
 
L1 = []
n1 = int(input("Enter number of elements : "))
for i in range(n1):
    e1 = int(input("Enter the elements of your list: "))
L.extend(L1)
print(L[::2])

#3.Write a Python program that takes a list of strings and returns a new list with only the strings that contain the letter "


#4. Write a Python program that takes a list of numbers and returns a new list with the numbers sorted in ascending order
L = []
 

n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    e = int(input("Enter your elements:"))
    
    L.append(e)
    L.sort()

print(L)
#5. Write a Python program that takes a list of strings and returns a new list with the strings sorted by length, from shortest to longest.
L = []
 

n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    e = input("Enter the element:")
    
    L.append(e)
    L.sort()

print(L)

#6. Write a Python program that takes a list of numbers and returns the product of all the numbers in the list.

#7.Write a Python program that takes a list of strings and returns the longest string in the list.

L = []
 

n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    e = input("Enter the element:")
    
    L.append(e)
    L.max()

print(L)























