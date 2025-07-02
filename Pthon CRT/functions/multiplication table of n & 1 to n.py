'''
Write a python program to build a function which prints the multiplication table of n
'''
def Table(Num):
    for i in range(1,11):
        print(f"{Num}x{i}={Num*i}")
Table(5)
#1 to n
def Table(Num):
    for i in range(1,Num+1):
        print(f"Multiplication Table of {i}")
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
Table(3)