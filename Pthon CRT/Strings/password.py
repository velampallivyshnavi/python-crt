'''
Write a python program to read password as input from the user and check whether it is a valid password or invalid password
'''
'''
Write a python program to read name contact number mail id and password and make sure that contact number has 10 digits and mail should have a valid structure following name@org,com and password should have atleast 3 uppercase,3 lower case,3 special characters and 1 number and length of the password not less than 10
'''
'''
Write a python program to read a string as input from the user and split the string into 3 equal halfs using slicing
'''
password=input("Enter your password :")
if len(password)<6:
    print("Invalid password")
elif not any(char.isdigit() for char in password):
    print("Invalid password (No digit)")
elif not any(char.isalpha() for char in password):
    print("Invalid password (No letter)")
else:
    print("Valid password")