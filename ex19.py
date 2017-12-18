# Variable is your functions are not connected to your scripts
# Creating the function, then formats the variables inside


def Tyranid_Models(Box_count, Tyranids):
    print(f"You have {Box_count} boxes!")
    print(f"You have {Tyranids} models of Tyranids!")
    print("That's a lot of units!")
    print("RUSH!!!")


# Directly giving values to use in function 'Tyranid_Models'
print("We can just give the function #'s directly:")
Tyranid_Models(200, 300)

print("Or, we can use variables from our script:")
# Creating variables, with # values
amount_of_Tyranids = 20
amount_of_boxes = 100

# The variables are called by the function and printed
Tyranid_Models(amount_of_Tyranids, amount_of_boxes)

print("We can even do math inside too:")
# Placing arithmatic as values for function 'Tyranid_Models'
Tyranid_Models(100 + 200, 500 + 600)

print("And we can combine the two, variables and math:")
# Using previous variables and arithmatic as values for function used
Tyranid_Models(amount_of_Tyranids + 100, amount_of_boxes + 1000)

# print(Tyranid_Models(amount_of_boxes, amount_of_Tyranids))
# This prints out none at the end, Why?


# Study Drill: Made my own Function
# Using int() changes value to a integer for arithmatic
def Vallejo_Paint(Own, Want):
    print(f"Colors I own: {Own}")
    print(f"Colors I want: {Want}")


# Directly placing values for function 'Vallejo_Paint'
print("I just bought a new color:")
Vallejo_Paint('Ivory', 'Teal')

print("I bought more colors:")
# Created Variable 'Ivory' added string
Ivory = 'White'
# Concatenated 'Ivory' and ', Teal' into 'Vallejo_Paint'
Vallejo_Paint(Ivory + ', Teal', 'Black')

print("I finally have the paints I need:")
# Variable using string concatenation is Concatenated into function
# Want in 'Vallejo_Paint' is given a value of 0
Ivory = 'White' + ', Teal'
Vallejo_Paint(Ivory + ', Black', 0)

# Multi line string w/ escape sequence newline
print("""Any paints you think I need?
\nI will add it to the list:""")
# 'paints' is given string as a value
# 'paint' is being called, input for function variable 'Want'
paints = 'White, Teal, Black'
Vallejo_Paint(paints, input())


# Created a function that uses multiplication and variables


def multiply(x):
    return 2 * x


multiply_2 = multiply(2)
print(multiply_2)
print("2 * 2 = {}".format(multiply_2))
