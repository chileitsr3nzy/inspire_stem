#program that gets sum of the first 20 numbers
#Date : 26/02/2024
#Name : Renish Nkirote

sum_num = 0
for x in range (0,21) :
    max_value =int(input("enter the maximum number"))
    for x in range (0 , max_value + 1):
        sum_num = sum_num + x
        print(sum_num)


