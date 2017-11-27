# \t tells Python to tab in the read line
tabby_cat = "\tI'm a tabby cat."

# \n tells Python to read on next line
persian_cat = "I'm split\non a line."

# \\ Is the Escape_Sequence for \
backslash_cat = "I'm \\ a \\ cat."

# Creating a multi_line string
# Using Escape_Sequences to print on new lines and tab
fat_cat = """
I \ will \ \\\ create \\\ a new list:
\t *NEKO
\t *ATSUME
\t *IS\n\t *COOL
"""

test = '''
This is a test for using \'
\t\nYup looked like it worked.
'''
formatter = "\t\n{}, {}, {}"

# Printing following variabeles
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(test)

# Introducing formatting to following variables
print(formatter.format(tabby_cat, persian_cat, backslash_cat,
      fat_cat))
