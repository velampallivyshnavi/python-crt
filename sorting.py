a=[56,2,44,58,10,33]
print(f"original array :{a}")
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)