s= [1,3,4,"apple",5.6,7]
s1= 0
try:
    for i in s:
        s1 += i
except:
    print("string appeared, last sum calculated: ", s1)
else:
    print(s1)

try:
    s = ""
    while True:
        
        s1 = eval(input("Enter the string: "))
        s += s1
except:
    print(s)
