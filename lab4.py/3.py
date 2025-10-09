import math

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)


h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
area = 0.5 * (b1 + b2) * h
print("Expected Output:", area)


n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = n * s * s / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)


base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)
