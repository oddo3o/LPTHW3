types_of_people = 10

# Formatting value '10' into variable 'x'
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# String-ception # 1
# Formatting both strings 'binary' and do_not into 'y'
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# String-ception # 2
# Formatting 'x' and print
print(f"I said: {x}")

# String-ception # 3
# Formatting 'y' and print
print(f"I also said: '{y}'")

# False is a boolean value
hilarious = False
joke_evaluation = "Isn't that joke funny? {}"

# Formatting 'hilarious' into 'joke_evaluation' then print
print(joke_evaluation.format(hilarious))

# Creating strings
w = "This is the left side of ..."
e = " a string with a right side."

# String-ception # 4
# Using special character '+' to combine strings 'concatenates'
print(w + e)
