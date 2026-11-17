#Exceptions
#1.try
#2.accept
#3.else
#4.finally
try:
    a=1
    b="abc"
    c=(a/b)
    print(c)
except TypeError:
    print("Check 'b' it is a string")
except:
    print("can not divide by Zero")
else:
    print(c)
finally:
    print("Finally is running")

##x = eval(input("Enter a number: "))
##if type(x) != int:
##         raise exception("Enter only int values")
##        else:
##            print(x)
