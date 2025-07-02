'''
Write a python program to:
.Take a list of Names(some repeated)
.Remove duplicates
Sort and display the final toy list to pack
'''
size=int(input("Enter the Size of List :"))
Toy_List=[]
NewToy_List=[]
for i in range(size):
    Temp=input(f"Enter the Integer Value at {i} index :")
    Toy_List.append(Temp)
print(Toy_List)
for i  in Toy_List:
    if i not in NewToy_List:
        NewToy_List.append(i)
print("After removing duplicates",NewToy_List)
NewToy_List.sort()
print("After sorting",NewToy_List)

