# Creating string with open ' ' for user input
# Places in ' ' the most recent input
print("How old are you?", end=' ')
# Yup this proves that end=' ' uses most recent input
# print(22)

# PLacing user input into variable 'age'
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

thinking = "..."
# Combining formatting above variables into string
# Using Escape_Sequence to repositon string
print("""\nSo you\'re {} years old, {} tall and weigh {} \n{}
NICE <3""".format(age, height, weight, thinking * 5))

# Testing this out to see if variables are recallable
# *Spoiler* They are recallable
# print(age)
# print(height)
# print(weight)

# Spice it up
# Running user input as a integer to do math
print("\nWe will go 5 years into the future.")
print(thinking * 5)
print("What's your age again?", end=' ')
print(int(input()) + 5)
math = input()
print("Behold my power!!!")
