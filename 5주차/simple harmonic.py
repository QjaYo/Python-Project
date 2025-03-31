from vpython import *

A = 1
w = 1
gh1 = graph(title = "simple harmonic", xtitle = 't', ytitle = 'y')
f_rt = gcurve(graph = gh1, color = color.black, label = "r(t)")
f_vt = gcurve(graph = gh1, color = color.blue , label = "v(t)")
f_at = gcurve(graph = gh1, color = color.red, label = "a(t)")

for t in arange(-10, 10, 0.01):
  f_rt.plot(pos = (t, A * sin(w*t)))
  f_vt.plot(pos = (t, w * A * cos(w*t)))
  f_at.plot(pos = (t, (-1) * w**2 * sin(w*t)))

input()