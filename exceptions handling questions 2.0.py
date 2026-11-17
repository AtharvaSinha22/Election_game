#1
try:
  x = int(input("Enter a number: "))
except:
       print("Enter a number")
finally:
  print("Program is not working because its a string")

#2.
i = int(input("Enter a number: "))
x = int(input("Enter a number: "))

if x == 0:
  raise Exception("Cannot divide by 0")
else:
  print(i/x)


#3.
L = [1,2,3,"apple",3.5,"cherry"]
try:
  p =1
  for i in  L:
    p *=1
except ValueError:
  print("Check for the Values")
except TypeError:
  print("Check type of elements")
else:
  print (p)
