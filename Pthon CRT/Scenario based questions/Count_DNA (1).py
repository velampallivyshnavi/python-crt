'''
write a program that
checks if the string has only valid bases(A,T,G,C)
then count how many of each base there are.
'''
base=input("Enter the Sample Base Value :")
A,T,C,G=0,0,0,0
for i in base:
    if i=='A':
        A+=1
    if i=='T':
        T+=1
    if i=='C':
        C+=1
    if i=='G':
        G+=1
new_base={'A':A,'T':T,'C':C,'G':G}
print(new_base)
#another method
sequence=input("Enter the sequence in ATGC :")
base_count={'A':sequence.count('A'),'T':sequence.count('T'),'G':sequence.count('G'),'C':sequence.count('C'),}
print(base_count)