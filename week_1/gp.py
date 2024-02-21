#this is a program to generate the terms and sum in geometric progression
#Date : 20/02/2024
#Name : Renish Nkirote 

a = int(input("enter the first term: "))
r = int(input("enter the common ration: "))
n = int(input("enter the number of the terms: "))

sum = 0
term = a

for i in range(n):
    print(term, end=" ")
    sum+= term
    term*= r 
    print("\n the sum of the geometri progression is",sum)
