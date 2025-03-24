from vpython import *

step = 1
def key_input(evt):
    s = evt.key
    cam = scene.camera
    if s == 'left':
        cam.pos += vector(-step, 0, 0)  # 왼쪽
    elif s == 'right':
        cam.pos += vector(step, 0, 0)   # 오른쪽
    elif s == 'up':
        cam.pos += vector(0, step, 0)   # 위로
    elif s == 'down':
        cam.pos += vector(0, -step, 0)  # 아래로
scene.bind('keydown', key_input)