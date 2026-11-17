'''#"If" condition
x=10
if x>0:
    print("x is positive")

Text="Hello world"
if len(Text)>10:
    print("string is not empty")

x=0
if x>0:
    print("x is positive")
elif x<0:
    print("x is negitive")
  
else:
    print("x=0")

x=int(input("Enter a number:"))
if x%2!=0:
    print("x is odd number")

else:
    print("x is even number")

#chained condition
a=100
b=35
if a>0 and b>0: #and- if both conditions are true only then code will work
    print(" a and b are positive")
else:
    print("a and b are negitive numbers")
a=100
b=35
if a>0 or b>0: #or- if any conditions are true only then code will work
    print(" a and b are positive")
else:
    print("a and b are negitive numbers")'''
#slicing
p=input("Enter a word:")
if p == p[::-1]:
    print("it's a palindrome")
else:
    print("it's not a palindromre")






















       
