#strings in python
#Date : 22/02/2024
#Name : Renish Nkirote


city = "nairobi"

print(city[0])# n
print(city[1])# a
print(city[2])# i
print(city[3])# r
print(city[4])# o
print(city[-1])# b
print(city[-2])# i


#convert to uppercase

print(city) 

print("\n\n")
print(city.upper())

name="RENISH NKIROTE"
print(name)
print(name.lower()) # converts print to lower case

town ="  Naivasha  "

print(town)
print("\t") # new tab
print(town.strip())

f_name = "Renish"
s_name = "Nkirote"

full_name = f_name + s_name
print(full_name)

city = "nairob"

#replacing a charater 

fruit = "orangeooooo"

print(fruit.replace('o' , 'y'))

subject = "Physicall,sciences"
print(subject.split(","))

age = 26
height = 1.76

print("i am {0} years old  and {1}metres tall " . format(age,height))