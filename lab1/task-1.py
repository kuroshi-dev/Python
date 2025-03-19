import math

print("Task 1: Calculate the value of z")

def init():
    """
    Initializes variables.
    """
    n = int(input("Enter n: ")); m = int(input("Enter m: "))
    return n, m

n, m = init() # Initialization of variables from function init()

if n >= 1 and m >= 1: # Validator
    print("")
else: # Error message
    print("Invalid input! Print n and m should be greater than or equal to 1.")
    n, m = init()

def calculate():
    """
    Calculates the value of z.
    """
    global z
    z = (math.sqrt(2) - math.sqrt(3*n))/(2*m)
    return z

z = calculate() # Initialization of z from function calculate()

print("z = ", z) # Output of z
