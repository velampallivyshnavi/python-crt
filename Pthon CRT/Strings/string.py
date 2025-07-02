'''
Write a python program to read input string from the user:
1.reverse the string
2.convert the string into lower case
3.convert the sting into upper case
4.convert the character of string to lower case if it is in upper case and convert to upper case if it is in lower case
5.check if the string is starting with the letter a
6.print the count of the character a from the given string and replace all p's to letter j
'''

Str=input("Enter the String :")
print(Str[::-1])
print(Str.lower())
print(Str.upper())
print(Str.swapcase())
print(Str.startswith('p'))
print(Str.count('p'))
Str=Str.lower()
print(Str.replace('p','j'))