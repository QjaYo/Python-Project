from vpython import *

def initAxis_xyz(size):
  x_axis = arrow(pos = vec(0, 0, 0), axis = vec(size, 0, 0), color = color.red, shaftwidth = 0.3)
  y_axis = arrow(pos = vec(0, 0, 0), axis = vec(0, size, 0), color = color.green, shaftwidth = 0.3)
  #z_axis = arrow(pos = vec(0, 0, 0), axis = vec(0, 0, size), color = color.blue, shaftwidth = 0.3)
  return x_axis, y_axis

initAxis_xyz(5)

theta = 0
r = (vec(cos(theta), sin(theta), 0))

v = vec(3, 4, 0)
v_par = dot(v, r) * r
v_per = v - v_par

dt = 0.01

r_arrow = arrow(axis = r, color = color.white, shaftwidth = 0.2)
v_arrow = arrow(axis = v, color = color.orange, shaftwidth = 0.2)
v_par_arrow = arrow(axis = v_par, color = color.yellow, shaftwidth = 0.2)
v_per_arrow = arrow(axis = v_per, color = color.purple, shaftwidth = 0.2)

while(1):
  rate(100)

  theta += dt

  r.x = cos(theta)
  r.y = sin(theta)
  r = hat(r)

  v_par = dot(v, r) * r
  v_per = v - v_par

  r_arrow.axis = r
  v_par_arrow.axis = v_par
  v_per_arrow.axis = v_per
  

input()