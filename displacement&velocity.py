from vpython import *

ri = vec(2, 4, 0)
ti = 0

rf = vec(3, 3.5, 0)
tf = 0.2

dr = rf- ri
dt = tf - ti
v_avg = dr / dt

dr_vec = arrow(axis = dr, color = color.red, shaftwidth = 0.2)
v_avg_vec = arrow(axis = v_avg, color = color.green, shaftwidth = 0.2)

input()