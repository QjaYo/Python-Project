from vpython import *
import controls


#SHAPE
r = [] #list()도 가능
obj = []

ground = box(pos = vec(0, 0, 0), size = vec(15, 1, 15))

for i in range(100):
  obj.append(sphere(pos = vec(0, 1, 0), radius = 0.1, color = vec(random(), random(), random()), make_trail = True, retain = 30))
    #random 0~1
    #make trail 자취남기기
    #retain 꼬리길이

#INIT PARAMETER
vi = vec(0, 15, 0) #초기속도
a = vec(0, -9.8, 0) #가속도
t = 0
dt = 0.01

explosion = False

for elem in obj:
  elem.v = vi

#SIMULATION LOOP
while (t < 100):
  rate(1 / dt)

  #explosion event
  if (t > 1 and explosion == False):
    print("explosion")
    explosion = True
    for elem in obj:
      vp = vec(random() - 0.5, random() - 0.5, random() - 0.5)
      elem.v += vp

  for elem in obj:
    #euler-cromer
    elem.v += a * dt
    elem.pos += elem.v * dt
    #collision with ground
    if (elem.pos.y < ground.pos.y):
      elem.pos.y = ground.pos.y
      elem.v.y *= -0.8
  
  t += dt



input()