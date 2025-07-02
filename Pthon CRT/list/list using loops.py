#         0   1  2  3  4 5  6  7   8
Num_list=[10,20,30,40,50,60,70,80,90]
#         -9 -8 -7 -6 -5 -4 -3 -2 -1
print(Num_list)
print("Accessing the List Elements using for loop without indexing")
for i in Num_list:
    print(i)
print("Acessing the List Elements using for loop with indexing")
for i in range(len(Num_list)):
    print(Num_list[i])
#using while loop
print("Accesing the list Elements using while loop without indexing")
i=0
while(i<len(Num_list)):
    print(Num_list[i])
    i+=1