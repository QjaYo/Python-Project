from vpython import *

a = vec(3, 4, 5)
b = vec(1, 4, 3)

c = a + b
d = a - b
print(c, d)

e = dot(a, b)
print(e)

theta1 = acos(e / (a.mag * b.mag))
print(theta1)
theta2 = degrees(theta1)
print(theta2)

print(diff_angle(a, b))
print(degrees(diff_angle(a, b)))

input()