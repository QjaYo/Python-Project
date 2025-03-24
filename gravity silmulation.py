from vpython import *

x_axis = arrow(pos = vec(0, 0, 0), axis = vec(100, 0, 0), color = color.red, shaftwidth = 0.3)
y_axis = arrow(pos = vec(0, 0, 0), axis = vec(0, 50, 0), color = color.green, shaftwidth = 0.3)

theta = pi / 4
direction = vec(cos(theta), sin(theta), 0)
speed = 20
velocity = speed * direction

g = vec(0, -9.8, 0)

stone = sphere(pos = vec(0, 10, 0), radius = 2, texture = textures.rock)

wall = box(pos = vec(50, 0, 0), )

dt = 0.01

n_brick = 10
brick_width = 2
brick_height = 2
brick_depth = 1
brick_x = 50
brick_y = brick_height / 2
for i in range(n_brick):
  box(pos = vec(brick_x, brick_y, 0), size = vec(brick_width, brick_height, brick_depth), texture = textures.wood)
  brick_y += brick_height

while(1):
  rate(100)
  stone.pos += velocity * dt
  velocity += g * dt

  if (stone.pos.y - stone.radius <= 0):
    velocity.y *= -1
    velocity *= 0.8

  

input()