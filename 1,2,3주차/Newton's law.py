from vpython import *
import math

sf = 5.0
G = 6.67e-11

earth = sphere(pos = vec(0,0,0), radius = sf*6378000, texture = textures.earth)
earth.mass = 5.974e24

moon = sphere(pos = vec(384400000, 0 , 0), radius = sf*1737000, texture = textures.rock)
moon.mass = 7.347e22


r = moon.pos - earth.pos
moon.force = - G * earth.mass * moon.mass / mag(r)**2 * hat(r)
r = earth.pos - moon.pos
earth.force = - G * earth.mass * moon.mass / mag(r)**2 * hat(r)

moon.acc = moon.force / moon.mass
earth.acc = earth.force / earth.mass

print("Force of moon = ", moon.force)
print("Force of earth = ", earth.force)
print("Acc of moon = ", moon.acc)
print("Acc of earth = ", earth.acc)

input()