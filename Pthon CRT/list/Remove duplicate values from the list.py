List=[5,5,19,19,2,2]
print("Original List :")
print(List)
New_List=[]
for i in List:
    if i not in New_List:
        New_List.append(i)
print(New_List)
