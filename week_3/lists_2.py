friends = ["Bridgett","Faith","Michael","Wayne","Lizabel"]
for friend in friends :
    print(friend)


enemies=friends[:] #copy one list into another
for enemy in enemies:
    print(enemy)

fruits =["guava","pinneaples","mango","apple","oranges"]


print(fruits[0:3])
del fruits[0]
print(fruits)

squares= []#initializes an empty list

for x in range(0,11):
    squares.append(x**2)

print(squares)