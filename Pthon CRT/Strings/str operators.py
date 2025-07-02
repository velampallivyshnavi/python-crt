#To print address
a=10
b=10
print(id(a))
print(id(b))
#To print address for one string one int
a=10
b='10'
print(id(a))
print(id(b))
#To print a=b or not in int
a=10
b=10
print(a is b)
#To print a=b or using string and int
a=10
b='10'
print(a is b)

#string operators
''' three types:
1. basic operators:
    two types:
    1.string replication(*)
    2.string concatination(+)
2.member ship operators
    two types:
    1.in
    2.not in
3.comparision operator:>,<,>=,<=,!=
'''

#multiple prints using slicing operator
"$" * 7
str1="Students"
print(str1*5)
print(str1[0:4]*3)

#slicing
str="Python Program"
print(str[1:6])
print(str[0])
print(str[7:11])
print(str[10:14])
print(str[7:10])
print(str[2:6])
print(str[::-1])
print(str[5::-1]) or print(str[-9::-1])
print(str[-1:-8:-1])
print(str[-4:-8:-1])

#concatenation operator
a="Hello"
b=" World"
c=a+b
print(c)