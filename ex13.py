# import module is used with the argument variable
from sys import argv

# read the WYSS section for how to run this
# Each input in command line is assigned to a variale
script, first, second, third = argv

# User input for variales
print("Give my the script name:")
script = input()
print("I will need a value now:")
first = input()
print("Add anything to this variable:")
second = input()
print("Add another variable:")
third = input()

# Argv needs to have 4 variables total any less/more won't run
# Variables are called and printed
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Int() to change assigned values to integers for arithmatic
print("Adding 4 to first variable:")
print(4 + int(first))
