##################
# Homework 1 (Given a side of square. Find its perimeter and area)
##################
side = float(input("Enter side of square: "))
print("Perimeter =", 4 * side)
print("Area =", side ** 2)
##################
# Homework 2 (Given diameter of circle. Find its length)
##################
diameter = float(input("Enter the diameter of the circle: "))
pi = 3.14159
length = pi * diameter
print(f"Length (circumference) of circle = {length}")
##################
# Homework 3 (Given two numbers a and b. Find their mean)
##################
A = float(input("Enter the length of side A: "))
B = float(input("Enter the length of side B: "))
mean = (A + B) / 2
print("Mean =", mean)
##################
# Homework 4 (Given two numbers a and b. Find their sum, product and square of each number) 
##################
A=float(input("For the first number, enter A: "))
B=float(input("For the second number, enter B: "))
print("Sum =", A + B)
print("Product =", A * B)
print("Square of A =", A ** 2)
print("Square of B =", B ** 2)
