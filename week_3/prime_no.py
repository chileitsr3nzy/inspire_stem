


lower_value = 1
upper_value = 99  
  
print ("Prime numbers between {0} and {1} are :".format(lower_value , upper_value))

for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
