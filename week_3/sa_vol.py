



#A program that calculates the surface area & volume of a cylinder ,cone, cube, sphere
#Date :29/02/2024
#Name :Rensh Nkirote

import math

def sa_volume (radius ,height):
    #Cylinder
    cylinder_sa = 2 * math.pi * radius *(radius + height)
    cylinder_vol = math.pi * (radius**2) * height

    #Cone
    cone_length = (radius + 7) 
    cone_sa = (math.pi * (radius**2)) + (math.pi * radius * cone_length)
    cone_vol = (1/3) * math.pi * (radius**3)

    #Cube
    l = radius 
    cube_sa = 6 * (l **2) 
    cube_vol = l**3

    #Sphere
    sphere_sa = 4 * math.pi * (radius**2)
    sphere_vol = (4/3) * math.pi * (radius**3)

    print ("cylinder surface area: {0}, cylinder volume: {1} ".format(cylinder_sa, cylinder_vol))
    print ("cone surface area: {0}, cone volume: {1} ".format(cone_sa, cone_vol))
    print ("cube surface area: {0}, cube volume: {1} ".format(cube_sa, cube_vol))
    print ("sphere surface area: {0}, sphere volume: {1} ".format(sphere_sa, sphere_vol))

sa_volume(7,14)    

