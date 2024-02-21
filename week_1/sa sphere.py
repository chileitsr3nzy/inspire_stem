#this is a program that calculates the surface area of a sphere
#Date : 20/02/2024
#Name : Renish Nkirote

import math
 
r = float(input("enter the radius of th sphere : "))
surface_area = 4 * math.pi * pow(r, 2)

print("The surface area of the sphere is {:.2f}".format(surface_area))

