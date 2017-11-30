# Using import module on argv
from sys import argv

# Assigning values to variables in command line with argv
script, user_name, day = argv
# Assigning '> ' to variable prompt
prompt = '... '

# Format statement user_name / script, in command line
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

# Format statement user_name
print(f"Do you like me {user_name}?")

# Creating variable likes, user input calling variable prompt
likes = input(prompt)

# Format statememt user_name
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Printing multi-line format statement with variables
# likes, lives, computer
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

print("So how's your day?")
print(f"{day}, sounds like a nice time. Nice.")
