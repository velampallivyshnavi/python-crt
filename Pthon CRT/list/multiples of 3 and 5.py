List=[]
Len=int(input("Enter the Size of List :"))
New_List=[]
for i in range(Len):
    Temp=int(input(f"Enter the Integer Value at {i} index :"))
    List.append(Temp)
print("Given List:")
print(List)
for i in List:
    if i%5==0 and i%3==0:
        New_List.append(i)
print("List of 3 and 5 Multiples :")
print(New_List)

