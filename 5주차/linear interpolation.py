from vpython import *

def biInterpolation(pos, dx, dy, grid):
  cellx = int(pos.x / dx)
  celly = int(pos.y / dy)
  cellbox = box(pos =vec((cellx + 0.5) * dx ))