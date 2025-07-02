'''
Write a python program to:
.Add 10 songs to a playlist
.Show the playlist in normal and reverse order
'''
size=10
Songs_List=[]
for i in range(size):
    Temp=input(f"Enter the Integer Value at {i} index :")
    Songs_List.append(Temp)
print(Songs_List)
print(Songs_List[::-1])
