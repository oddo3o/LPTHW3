name = 'Christian'
age = 22  # No one likes you when you're 22
height = 64  # inches
weight = 120  # since highschool :(
eyes = 'brown'  # Pretty brown eyes Nujabes
hair = 'black'
teeth = 'white - ish'  # yeah needs work

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This is integrating some math with variables.

total = age + height + weight
print(f"If I add {age}, {height}, and {weight}"
      f" I get {total}.")

# Convert Inches to Centimeters.

cm = 2.54
centi = round(cm * height)
print(f"This is my height in inches {height}, this is my height in"
      f" centimeters {centi}.")

# Convert pounds to Kilograms.

kg = 0.453592
kilo = round(kg * weight)

print(f"This is my weight in pounds {weight}, this is my weight in"
      f" kilograms {kilo}.")
