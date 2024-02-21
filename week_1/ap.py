#program to determine the arithmetic progression of sequences
#Date : 20/02/2024
#Name : Renish Nkirote

a = int(input("enter the first term: "))
d = int(input("enter the common difference: "))
n = int(input ("enter the number of the terms: "))

sum = 0
term = a 

for i in range(n):
    print (term, end =" ")
    sum += term
    term += d

    print("\n The sum of the arithmetic progression is", sum)