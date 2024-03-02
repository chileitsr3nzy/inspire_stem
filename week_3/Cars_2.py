#this is a list that describes cars


class car:
    def __init__(self,model,make, year_of_production, fuel,capacity,colour,):
       self.model = model 
       self.make = make
       self.year_of_production = year_of_production
       self.fuel= fuel
       self.capacity= capacity
       self.colour =colour 

    def print_make(self,make):
        print("The car is {0}make".format(self.make))
    
    def set_make(self,make):
        self.make = make
    
    def get_make(self):
        return self.make

my_car = car("impalla","chevrolet","2500cc","lilac")
friends_car = ("note","nissan","2014","1400cc","black")

my_car.print_make("nissan")

my_car.set_make("ford")

friends_car.set_make("Toyota")

print(my_car.get_make())
print(friends_car.get_make())