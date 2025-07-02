'''
Write a python program to print uppercase alphabets from a to z including the ASCII values
'''

for i in range(1,27):
    print(chr(i+64),"------>",i+64)
print("-------------")
for i in range(1,27):
    print(chr(i+96),"-------->",i+96)

'''
Write a python program to read a character as input from the user and print ASCII values of the character
'''
char=input("Enter the character :")
print(ord(char))