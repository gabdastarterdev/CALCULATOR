# My 3 weeks of learning Python.
# I wanted to see if i learned anything.
# So i decided to make a calculator program.

# Made by: Gab!
# 10/18/2024

import math

# "+" As for Addition.
# "-" As for Subtraction.
# "x" As for Multiplication.
operator = input("Enter operator (+ - x): ")
print()

# Addition 
if operator == "+":
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 + num2
    print()
    print (f"Sum: {sum}")

# Subtraction
elif operator == "-":
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 - num2
    print()
    print (f"Sum: {sum}")

# Multiplication
elif operator == "x":
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    sum = num1 * num2
    print()
    print (f"Sum: {sum}")
    
# Error statements!

# Error 1
elif operator == " ":
    print("Invalid. Reason: No operator.")
    
# Error 2
# End of if statements.
else:
    print(f"Invalid {operator}. is not an operator")
