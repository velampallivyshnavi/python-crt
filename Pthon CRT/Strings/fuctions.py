'''
Write a python program to read a string as a input from the user
a) print count of upper case letters
b) print count of lower case letters
c) print the count of numeric values
d) print the count of special characters
'''
Str=input("Enter the String :")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
Special_Char=0
for ch in Str:
    if ch.isupper():
        Uppercase_Alpha=+1
    elif ch.islower():
        Lowercase_Alpha=+1
    elif ch.isdigit():
        Numeric=+1
    else:
        Special_Char=+1
print(f"Count of Upper case letters :{Uppercase_Alpha}")
print(f"Count of Lower case letters :{Lowercase_Alpha}")
print(f"Count of Numeric values :{Numeric}")
print(f"Count of Special characters :{Special_Char}")