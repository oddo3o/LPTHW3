# Powershell isn't running unicode 8 characters

# Importing to system 'script\encoding\error' from command line into
# sys.argv
import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# Function called 'main' formats language_file\encoding\errors
# into script
# varible 'line' calls 'language_file' with file command readline()
# if-statement: if line is true, run function 'print_line' format
# line\encoding\errors
# Return function 'main' formatting language_file\encoding\errors


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
# Function 'print_line' formats line\encoding\errors
# Variable next_lang calls variable 'line' using file command .strip
# Breaking the read file in variable 'line' into raw_bytes
# Variable 'raw_bytes' calls variable 'next_lang' with file command .encode
# Encoding raw_bytes for python to interpret
# Variable 'cooked_string' calls variable 'raw_bytes' with file command .decode
# Python interprets decoded


languages = open("ex23.txt", encoding="utf-8")

main(languages, encoding, error)
