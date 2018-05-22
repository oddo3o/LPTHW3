# Importing from sys mmodule argv
from sys import argv
# From command line script / input_file into module argv
script, input_file = argv


def print_all(f):
    print(f.read())
    # Function 'print_all' prints variable 'f' f.read reads the file


def rewind(f):
    f.seek(0)
    # Function 'rewind' reads variable 'f' f.seek moves file to the 0 byte


def print_a_line(line_count, f):
    print(line_count, f.readline())
    # Function 'print_a_line' counts lines with line_count of variable 'f'
    # f.readline() reads variable 'f'


current_file = open(input_file)
# Variable 'current_file' opens input_file in module argv

# Print, escape sequence \n starts next line of code on a newline
print("First let's print the whole file:\n")

# Function 'print_all' on variable 'current_file', printed on newline
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Function 'rewind' on variable 'current_file'
rewind(current_file)

print("Let's print three lines:")

# Python reads following lines in desending order, running in order
# variable current_line = 1
current_line = 1
# Function 'print_a_line' w/ variables 'current_line' / 'current_file'
# Printing line 1 of 'current_file' w/ line count infront
print_a_line(current_line, current_file)

# 'current_line' = 'current_line' + 1
# 'current_line' = 2
# +=string operation meaning use both add and equal operations
current_line += 1
# Function 'print_a_line' w/ variable 'current_line' / 'current_file'
# Printing line 2 of 'current_file' w/ line count infront
print_a_line(current_line, current_file)

# 'current_line' = 'current_line' + 1
# 'current_line' = 3
# += string operation meaning use both add and equal operations
current_line += 1
# Function 'print_a_line' w/ variables 'current_line' / 'current_file'
# Printing line 3 of 'current_file' w/ line count infront
print_a_line(current_line, current_file)
