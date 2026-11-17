#1. Write a python function to check if a string is a panlindrom(reads same from fowards and backwords). The function should return true or false

s = input("Enter a word: ")
if s==s[::-1]:
    print("True")
else:
    print("False")
#2.Write a Python function to count the number of vowels in a given string. The function should return the count of vowels

i = input("Enter some words: ")

i = i.lower()
x = i.count("a")
x1= i.count("e")
x2= i.count("i")
x3= i.count("o")
x4= i.count("u")

y = x+x1+x2+x3+x4
print("Number of vowels =",(y))

#3. Write a python program to reverse a string without using any built-in functions or slicing operations.
 
i = input("Enter a word: ")
i_reversed = i[::-1]
print(i_reversed)

#4. Write a python program to remove all duplicates from a string and return the modified string with only unique characters.
i = input("Enter a word: ")
s = 0
i1 = ""
for x in i:
    if i.index(x)== s:
        i1+=x
    s+=1
print(i1)

#5. Write a python function to check if two strings are anagrams The function should return True if the strings are anagrams and False otherwise.

str1 = input("Enter a word: ")
str2 = input("Enter a word: ")

if len(str1)!= len(str2):
    print("False")
else:
    if sorted(str1)==sorted(str2):
        print("True")

#6. Write a Python function to find the longest common prefix among a list of strings. If there is no common prefix, the function should return an empty string.

strings = ["flour","flower","flourish"]
strings.sort()
fst_string = strings[0]
last_string = strings[-1]

common = [] 
for i in range(len(fst_string)):

  if i<len(last_string)and fst_string[i] == last_string[i]:
    common.append(fst_string[i])
  else:
    break
print(common)

#7. Write a Python function to find the first non-repeating character in a string. If there are no non-repeating characters, the function should return none.



#8. Write a Python function to check if a string contains only digits. The function should return True if the string contains only digits and False otherwise
n = input("Enter a word: ")
print(n.isdigit())

#9.Write a Python function to capitalize the first letter of each word in a sentence. For example, if the input is "hello world", the function should return "Hello World".


s = input("Enter the word: ")
a = ""
s = s.split()
for i in s:
    a = a+""+i.capitalize()
    print(a)


#10.Write a python program that takes a list  of strings and returns a new list with the first and last character in the original list.

i = input("Enter your name: ")
for s in i:
    s.append(i[0]+i[-1])
    print(s)
