#File Handling

'''
read r
write w
append a
create x

'''

'''
text b
binary b
'''
##file = open(‪r'C:\Users\HP\Desktop\Demotxt.txt','w')
##file.write("/nData Appended in the new file.")
##print(file.read())
##file.close()
##
##file = open(r'C:\Users\HP\Desktop\India.txt.txt','x')
##file.write('''/nIndia is one of the strongest countries in the world.
##It is the seventh-largest country in the world area-wise and the second-most populous country in the world.
##India shares its borders with countries like Pakistan, Afghanistan, China, Nepal, Bhutan, Myanmar and Bangladesh.''')
##file.close()

file  = open(r'C:\Users\HP\Desktop\India.txt.txt','r')
print(file.read())
