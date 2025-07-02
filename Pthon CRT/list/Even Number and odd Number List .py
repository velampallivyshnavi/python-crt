'''
Write a python program to:
.Input a list of numbers
.Create two new lists:one for even numbers,odd for odd numbers
.Display both lists
'''
size=int(input("Enter the Size of List :"))
List=[]
for i in range(size):
    Temp=int(input("Enter the Element at {i} index :"))
    List.append(Temp)
Even_List=[]
Odd_List=[]
for i in List:
    if i%2==0:
        Even_List.append(i)
    else:
        Odd_List.append(i)
print("Even Numbers",Even_List)
print("Odd Numbers",Odd_List)
