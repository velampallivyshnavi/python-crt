'''
compare two strings of the same length and print the positions(indices)
where the sequence differ.
'''
seq1=input("Enter the First Sequence :")
seq2=input("Enter the Second Sequence :")
print(seq1)
print(seq2)
list=[]
if(len(seq1)==len(seq2)):
    for i in range(len(seq1)):
        if seq1[i] not in seq2[i]:
            list.append(i)
print(list)