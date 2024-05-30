import math

BEZEL_ALLOWANCE = 1

l = float(input("Monitor size (in, diag): ")) + BEZEL_ALLOWANCE
z = float(input("Monitor distance (in): "))

w = 0.872 * l
h = 0.49 * l

phi = math.atan(w /(2.0 * z))
theta = 2 * phi

total_width = round(w * (1 + math.cos(theta)))
total_length = round(w / 2 * math.sin(theta))
vert_angle = round(math.degrees(2 * math.atan(h / (2 * z))))

print("total_width: " + str(total_width) + "in")
print("total_length: " + str(total_length) + "in")
print("vert_angle: " + str(vert_angle) + "deg")