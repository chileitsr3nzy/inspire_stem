#this is a programm that calculates the surface area of a cylinder
#Date : 20/2/2024
#Name : Renish Nkirote

import math
radius = float(input("enter the radius of the cylinder : "))
height = float(input("enter the height of the cylinder : "))

surface_area = 2 * math.pi * radius * (radius + height )

print("the surface area of the cylinder is", surface_area)




