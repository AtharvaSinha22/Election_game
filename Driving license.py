age = int(input("Enter the Age: "))
n = input("Are you an Indian?:(Y/N) ")
pf = input("Are you physically fit?:(Y/N)")

if age > 18:
    if n == "Y":
        if pf == "Y":
            print("Eligible for Test")
elif age == 18:
    if n== "Y":
        if pf == "Y":
            print("Eligble for Test")
        else:
            print("Not Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
