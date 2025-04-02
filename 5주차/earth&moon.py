from vpython import *
import controls
import math

sf = 5.0
G = 6.67e-11

earth = sphere(pos = vec(0,0,0), radius = sf*6378000, texture = textures.earth, make_trail = True)
earth.mass = 5.974e24
earth.v = vec(0, 0, 0)

moon = sphere(pos = vec(384400000, 0 , 0), radius = sf*1737000, texture = textures.rock, make_trail = True)
moon.mass = 7.347e22
moon.v = vec(0, 0, 0)

t = 0
dt = 1

while (True):
  rate(10000)

  if (earth.radius + moon.radius >= mag(earth.pos - moon.pos)):
    print("Boom!")
    print(f"{t // (24 * 60 * 60)}day {(t % (24 * 60 * 60) // (60 * 60))}hour")
    break

  #3rdlaw, Gravity
  r = moon.pos - earth.pos
  moon.force = - G * earth.mass * moon.mass / mag(r)**2 * norm(r)
  moon.acc = moon.force / moon.mass

  r = earth.pos - moon.pos
  earth.force = - G * earth.mass * moon.mass / mag(r)**2 * norm(r)
  earth.acc = earth.force / earth.mass

  #euler-cromer method
  moon.v += moon.acc * dt
  moon.pos += moon.v * dt

  earth.v += earth.acc * dt
  earth.pos += earth.v * dt

  t += dt

input()