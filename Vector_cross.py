from vpython import *

a = vec(2, 3, 4)
b = vec(1, -1, 1)

c = cross(a, b)

a_arrow = arrow(axis = a, color = color.red, shaftwidth = 0.2)
b_arrow = arrow(axis = b, color = color.green, shaftwidth = 0.2)
c_arrow = arrow(axis = c, color = color.blue, shaftwidth = 0.2)
d_arrow = arrow(axis = cross(b, a), color = color.yellow, shaftwidth = 0.2)

input()