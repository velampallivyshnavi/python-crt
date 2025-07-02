'''
Transription simulation
turn DNA into RNA by replacing every T with U
write a loop to convert a DNA string to its RNA form
'''
sequence=input("Enter the sequence: ")
for i in sequence:
    Rep_Sequence=sequence.replace('T','U')
print(f"Converted Sequence :{Rep_Sequence}")