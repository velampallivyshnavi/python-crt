'''
Write a python program mail id as input from the user and print username and organisation name based on mail id(name@orgname.com)
'''

Mail_id=input("Enter the Mail_id :")
List=Mail_id.split('@')
print(f"User Name : {List[0]}")
Org=List[1]
List=Org.split('.')
print(List)
print(f"org Name :{List[0]}")