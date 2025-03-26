from vpython import *
import controls

#global variable
g = vec(0, -9.8, 0)

#shape
ball = sphere(radius = 0.2)

#init parameter
ball.pos = vec(-2, 0, 0)
ball.v = vec(10, 20, 0)
ball.a = g
attach_arrow(ball, "v", shaftwidth = 0.1, color = color.white)
attach_arrow(ball, "a", shaftwidth = 0.05, color = color.red)
attach_trail(ball, type = "curve", pps = 5)

#time setting
t = 0
dt = 0.01

#graph
motion_graph = graph(title = "position-time", xtitle = 't', ytitle = 'y')
g_bally = gcurve(color = color.black)
motion_graph = graph(title = "velocity-time", xtitle = 't', ytitle = 'v')
g_ballvy = gcurve(color = color.green)

#simulation loop

#euler-cromer
while (False):
  rate(1 / dt)
  ball.v = ball.v + ball.a * dt
  ball.pos = ball.pos + ball.v * dt
  t = t + dt

#euler
while (False):
  rate(1 / dt)
  ball.pos = ball.pos + ball.v * dt
  ball.v = ball.v + ball.a * dt
  t = t + dt

#semi-implicit
while (False):
  rate(1 / dt)
  ball.v_next = ball.v + ball.a * dt
  ball.pos = ball.pos + ((1/2) * (ball.v + ball.v_next)) * dt
  ball.v = ball.v_next
  t = t + dt

while (True):
  rate(1 / dt)
  ball.v_next = ball.v + ball.a * dt
  ball.pos = ball.pos + ((1/2) * (ball.v + ball.v_next)) * dt
  ball.v = ball.v_next

  #graph update
  g_bally.plot(pos = (t, ball.pos.y))
  g_ballvy.plot(pos = (t, ball.v.y))

  #time update
  t = t + dt