#Dictionary

d = {"Name": ["Surya","Arun"], "Age": 25}
##print(d,type(d))


#characterestics

'''
1.Key is used as an index
2.Ordered
3.Duplicates are allowed as values
4.Mutable
'''
##print(d.keys)
##print(d.values)
##print(d.items)
print(d.keys())
print(d.values())
print(d.items())

print(d["Age"])

d['Name'] = "Arun"
print(d.get('Name'))
d["Occupation"] = "Student"
print(d)
d.update({"Qualification":"12th Pass"})
print(d)

#Delete Elements

'''
pop()
del
clear()
'''
d.pop("Age")
print(d)

d.popitem()
print(d)

del d["Occupation"]
print(d)

d.clear()
print(d)

d1= {"Name":"Surya","Age":25}
for i in d1.items():
    print(i)





























