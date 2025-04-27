from vpython import *
import controls

#objects
ground = box(color = color.green, size = vec(100, 60, 0.3))
ball = sphere(radius = 0.11, pos = vec(-40, 0.11 + 0.15, 0), make_trail = True)

#init parameter
ball.mass = 0.45
ball.speed = 25
ball.angle = radians(35)
ball.v = ball.speed * vec(cos(ball.angle), sin(ball.angle), 0)
g = 9.8
rho = 1.204
Cd = 0.3
t = 0
dt = 0.01

#simulation loop
while (t < 20):

  rate(1 / dt)
  #force calculation
  gravity = ball.mass * vec(0, -g, 0)
  drag = (-0.5) * Cd * rho * (ball.radius**2 * pi) * mag(ball.v)**2 * norm(ball.v)
  ball.f = gravity + drag
  ball.a = ball.f / ball.mass

  #euler-cromer
  ball.v += ball.a * dt
  ball.pos = ball.pos + ball.v * dt
  
  #collision check
  if (ball.pos.y < ground.pos.y + 0.11 + 0.15):
    break

  t += dt

input()