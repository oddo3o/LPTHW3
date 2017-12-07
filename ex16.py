# Module import on argv
from sys import argv

# Assigning variables to argv
script, filename = argv

# F-string formatting "filename"
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# User input, Hitting return will run lines 15 - 37
input(":")

print("Opening the file...")
# Command open on "filename" is assigned to "target"
# "w" to open file in write mode
target = open(filename, 'w')

# Truncation is redundant because we are opening filename in "w" mode
# print("Truncating the file. Goodbye.")
# "target" is truncated
# target.truncate()

print("Now I'm going to ask you for three lines.")

# User Input assigned to variables "line1,2,3", Print "line 1 - 3:"
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# Lines 35 - 42 in one string
# Using f-string on "line#" and escape sequence \n
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
# "line1" written to "target"
# target.write(line1)
# Escape sequence \n, creates new line in "target"
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
print(f"We will print what's inside {filename}.")
# Returning the cursor back to 0 placement to print
target.seek(0)
# Default for open() is opening in read mode
print(open(filename).read())
print("And finally, we close it.")

# "target" is closed using function .close, preventing open lines
target.close()
