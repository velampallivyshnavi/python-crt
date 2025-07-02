List=[]
Len=int(input("Enter the Size of the List :"))
New_List=[]
for i in range(Len):
    Temp=int(input(f"Enter the integer value at {i} index :"))
    List.append(Temp)
print("Given List :")
print(List)
for i in List:
    if i%5==0:
        New_List.append(i)
print(New_List)

