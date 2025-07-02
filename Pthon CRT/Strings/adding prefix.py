'''
Write a python program to take name as input from the user including prefix(either MR or Miss) print the gender classification of the name on basis of prefix
'''

Str=input("Enter the Name:")
if(Str.startswith("Mr.")):
    print("Male")
elif(Str.startswith("Ms.")):
    print("Female")
else:
    print("In-valid Name")