'''
Write a python program to read the list of characters from the user and convert it into a word and print it
'''

Size=int(input("Enter the length of list :"))
Char_List=[]
for i in range(Size):
    ch=input("Enter the characters :")
    Char_List.append(ch)
print(Char_List)
Str="".join(Char_List)
print(Str)