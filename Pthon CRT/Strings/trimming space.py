#write a python program to read a string as the input from the user (including spaces) and print the string by trimming the spaces
Input=input("Enter the String :")
print(f"User Entered String :{Input}")
str_List=Input.split()
Res="".join(str_List)
print(f"String without spaces :{Res}")


Str1="Hey"
Str2="Hi"
print(Str1)
print(Str2)
S=Str1.join(Str2)



