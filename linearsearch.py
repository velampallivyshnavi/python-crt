arr=[5,6,2,3,4,1,0,7,8,9]
def linearsearch(key,arr,len):
    for i in range (len):
        if arr[i]==key:
            index=i
        else:
            index=i
            break
res=linearsearch(1,arr,10)
if res==-1:
    print("element not found")
else:
    print(f"element found at {res} index")