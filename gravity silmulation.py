from vpython import *
import controls

#global variable
n_brick = 20
brick_width = 2
brick_height = 2
brick_depth = 1
brick_x = 50
brick_y = brick_height / 2
boxes = []

#shape
x_axis = arrow(pos = vec(0, 0, 0), axis = vec(100, 0, 0), color = color.red, shaftwidth = 0.3)
y_axis = arrow(pos = vec(0, 0, 0), axis = vec(0, 50, 0), color = color.green, shaftwidth = 0.3)
stone = sphere(pos = vec(0, 10, 0), radius = 2, texture = textures.rock)
wall = box(pos = vec(50, 0, 0), size = vec(2, 2, 1))
for i in range(n_brick):
  box_temp = box(pos = vec(brick_x, brick_y, 0), size = vec(brick_width, brick_height, brick_depth), texture = textures.wood)
  boxes.append(box_temp)
  brick_y += brick_height


#init parameter
g = vec(0, -9.8, 0)
theta = pi / 6
direction = vec(cos(theta), sin(theta), 0)
speed = 40
velocity = speed * direction


#time setting
t = 0
dt = 0.01
t += dt



dt = 0.01


while(1):
  rate(100)
  stone.pos += velocity * dt
  velocity += g * dt

  if (stone.pos.y - stone.radius <= 0):
    velocity.y *= -1
    velocity *= 0.7

  for i in range(n_brick):
    if (boxes[i].pos.x - boxes[i].size.x / 2 <= stone.pos.x + stone.radius
        and boxes[i].pos.y + boxes[i].size.y / 2 >= stone.pos.y - stone.radius):
      velocity.x *= -1
      velocity *= 0.7
      break

  

input()