arr=[10,20,30,40,50.5,67,58,87]
length=len(arr)
print(f"original array :{arr}")
for i in range(length):
    for j in range(1,length):
        if(arr[i]>arr[j]):
         temp=arr[i]
         arr[i]=arr[j]
         arr[j]=temp
print(f"sorted array : {arr}")