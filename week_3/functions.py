def print_name():
    print("My name is Rensh Nkirote")


#calling the function
print_name()
print_name()
print_name()

def print_details(name,age,id,gender):
    print("i am {0}, {1}years old . My id no is{2} and gender is {3}" . format(name,age,id,gender))

print_details("Renish Nkirote","18","2006123","Female")
print_details("lizabel mwende","18","2007123","Female")

def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)
print(sum_nums(4,5))
def prod_nums(x,y):
    return x * y 
print(prod_nums(4,5))


def print_odds(first_number,last_number):
    for i in range (first_number,last_number):
        print(i %2)
print_odds(0,15)       

