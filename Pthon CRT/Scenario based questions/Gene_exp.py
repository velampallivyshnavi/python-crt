'''
based on the value ,you need to label each gene as:
"Underexpressed"(<5)
"Normal"(5 to 15)
"Overexpressed"(>15)
Look through the list and assign the correct label to each number
'''
n=int(input("Enter the count of data :"))
list=[]
gene=[]
for i in range(n):
    temp=float(input("Enter the values :"))
    list.append(temp)
for i in list:
    if i<5:
        gene.append("Underexpressed")
    elif i>=5 and i<=15:
        gene.append("Normal")
    else:
        gene.append("Overexpressed")
print(gene)