# Module import on argument variable
from sys import argv

# Argv assigns values to variables from command line
script, filename = argv

# Command open with variable filename is assigned to variable txt
txt = open(filename)

# f-string formating filename
print(f"Here's your file {filename}:")
# Print variable txt, variable filename is open and read then printed
print(txt.read())

# Opening a file using user input while code is running
# print("Type the filename:")

# User input assigned to variable
# file_again = input("> ")

# txt_again is assigned command open on variable file_again
# txt_again = open(file_again)

# Open file_again, using function .read to read file, then print
# print(txt_again.read())

# Terms command and function are interchangable
# For security and consistency limit use of input()

# Close open files to free up memory
txt.close()
# txt_again.close()
