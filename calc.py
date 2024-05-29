import math

l = input("Monitor size (in, diag): ")
z = input("monitor distance (in): ")

w = 0.872*l
h = 0.49 * l
phi = math.acos(2 * z / w)
theta = 2 * phi

total_width = w * (1 + math.cos(theta))
total_length = w / 2 * math.sin(theta)
vert_angle = 2 * math.atan(h / (2 * z))

println("total_width: " + total_width)
println("total_length: " + total_length)
println("vert_angle: " + vert_angle)