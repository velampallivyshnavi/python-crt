'''
write a program that:
Takes a DNA sequence as input(a string)
Calculates the GC content as a percentage
Classifies the sequence as:
"High GC" if GC% >60
"Moderate GC" if GC% is between 40 and 60
"Low GC" if GC% <= 40
'''
sequence=input("Enter the Sequence :")
total_base=len(sequence)
GC=0
for i in sequence:
    if i in 'GC':
        GC+=1
GC_Content=((GC)/total_base)*100
print(f"GC Content :{GC_Content:.2f}")
if GC_Content>60:
    print("Classification: High GC")
elif GC_Content>=40 and GC_Content<=60:
    print("Classification: Moderate GC")
else:
    print("Classification: Low GC")