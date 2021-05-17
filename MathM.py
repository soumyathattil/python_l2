'''
Using the built-in functions on Numbers perform following operations
a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
b) Find out the square root of a given number. (Use sqrt(x) function)
c) Generate random number between 0, and 1 ( use  random() function)
d) Generate random number between 10 and  500. (Use uniform() function)
e) Explore all Math and Random module functions  on a given number/ List.

'''
import random
import math

print("a) Round of the given floating point number")
x = input("enter the floating number1: ")
x = float(x)

y = input("enter the floating number2: ")
y = float(y)

print("ADDING THE NUMBERS: " ,x, "+" ,y,"=" , x + y)

print("Printing the round floating number1 =", round(x), "Rounding number2 = ", round(y))

print("b) Find out the square root of a given number.")
x = input("enter the number: ")
x = int(x)
print("Square root of the number is ", math.sqrt(x))

print("c) Generate random number between 0, and 1")
print(" Generate random number is ", random.randint(0,1))

print("d) Generate uniformly random number between 10 and  500.")
print(" Generate uniformly random number is ", random.randint(10,500))

print("d) Generate uniformly random number between 10 and  500.")
print(" Generate uniformly random number is ", random.randint(10,500))

