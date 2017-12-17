# Importing module argv from sys to read in command line
from sys import argv
# Imprting module exists from os.path
from os.path import exists

# Assigning values to argv in the command line
script, from_file, to_file = argv

# printing f-string, formatting 'from_file' and 'to_file'
print(f"Copying from {from_file} to {to_file}")

# We could do these two in one line
# in_file = open(from_file)
# indata = in_file.read()

# Variable indata, is using command open() and .read on 'from_file'
# This is opening the file first, then reading what is inside
indata = open(from_file).read()

# f-string is printed, formating 'indata', using len command
# len command reads the length of the variabe 'indata'
print(f"The input file is {len(indata)} bytes long")

# Importing command exists, this prints a True or False if exists
# print f-string, formating to_file and module exists
# module exists prints a boolean value if file exists
# the boolean value is formatted into the f-string then printed
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# User input, to run next block, if {exist(to_file)} prints true
input()

# variable 'out_file', command open() on 'to_file', opening in write
out_file = open(to_file, 'w')
# "out_file" will open() 'to_file' in write mode, using command write
# 'indata' will open() 'from_file' w/ command read
# 'indata' will be read then written into 'out_file'
out_file.write(indata)

print("Alright, all done.")

# closing opened files preventing open ended files from interacting
out_file.close()
# in_file.close()

# ; can be used to create breaks in scripts
