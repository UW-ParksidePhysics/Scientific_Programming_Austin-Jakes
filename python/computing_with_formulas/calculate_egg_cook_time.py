#Egg & Temp Specs
import numpy as np 
from math import pi
import math 

mass_egg_s = 47           #np.array([47,67])  
mass_egg_L = 67           #m Small egg,Large egg ~ grams

density = 1.038                          #rho g/cm^3
heat_capacity = 3.7                      #c Joules/gram(Kelvin)
thermal_conductivity = 5.4*10**-3        #k Watts/meter(Kelvin)   

t_original_egg_ft = 4                #np.array([4,20])        
t_original_egg_rt = 20               #T_o   Fridge, Room temp. ~ Celcius 

t_center_egg = 70                        #T_y ~ Celsius
t_boil_water = 100                       #T_w ~ Celcius

left_divisor = (thermal_conductivity*(pi**2)*((4/3)*pi)**.66)

#Left equation
t_left_sm_egg = (((mass_egg_s**.66)*heat_capacity*(density)**.33)/left_divisor) #small egg
t_left_lg_egg = (((mass_egg_L**.66)*heat_capacity*(density)**.33)/left_divisor) #large egg
#Right equation
t_right_fridge_temp = math.log((.76*((t_original_egg_ft - t_boil_water)/(t_center_egg - t_boil_water))))    #fridge temp
t_right_room_temp = math.log((.76*((t_original_egg_rt - t_boil_water)/(t_center_egg - t_boil_water))))      #room temp

#combine left and right equations 
sm_egg_fridge = t_left_sm_egg * t_right_fridge_temp
sm_egg_room = t_left_sm_egg * t_right_room_temp

lg_egg_fridge = t_left_lg_egg * t_right_fridge_temp
lg_egg_room = t_left_lg_egg * t_right_room_temp

#Convert to min
sm_egg_fridge_min = sm_egg_fridge / 60
sm_egg_room_min = sm_egg_room / 60
lg_egg_fridge_min = lg_egg_fridge /60
lg_egg_room_min = lg_egg_room / 60

#print outputs
print(f'small fridge {sm_egg_fridge_min:.1f} minutes')
print(f'small room {sm_egg_room_min:.1f} minutes')
print(f'large frige {lg_egg_fridge_min:.1f} minutes')
print(f'large room {lg_egg_room_min:.1f} minutes')