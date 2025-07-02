'''
Write a python program to read a string as a input from the user and print the count of
a) upper case vowels
b) lower case vowels
c) upper case consonants
d) lower case consonants
 '''

Str=input("Enter the String :")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha() and ch.isupper()):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha() and ch.lower()):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"Lower case Vowel count :{L_Vowels}")
print(f"Upper case Vowel count :{U_Vowels}")
print(f"Lower case Consonants count :{L_Consonants}")
print(f"Upper case Consanants count :{U_Consonants}")