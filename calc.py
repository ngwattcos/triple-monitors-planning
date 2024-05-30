import math

l = int(input("Monitor size (in, diag): "))
z = int(input("Monitor distance (in): "))

w = 0.872 * l
h = 0.49 * l
phi = math.acos(2 * z / w)
theta = 2 * phi

total_width = math.round(w * (1 + math.cos(theta)))
total_length = math.round(w / 2 * math.sin(theta))
vert_angle = math.round(math.degrees(2 * math.atan(h / (2 * z))))

print("total_width: " + total_width)
print("total_length: " + total_length)
print("vert_angle: " + vert_angle)