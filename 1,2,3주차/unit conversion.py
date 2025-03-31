from vpython import *

#Usain Bolt 100m : 9.58

bolt_speed = 100 / 9.58
print(bolt_speed, "m/s")

bolt_speed = 0.1 / (9.58 / 60 / 60)
print(f"{bolt_speed:.4f}", "km/h")

#1.6mile = 1 km
bolt_speed = bolt_speed / 1.6
print(f"{bolt_speed:.4f}", "mph")

print(f"Bolt speed is {bolt_speed:.4f}mph")