def add(a, b):
    print(f"ADDING {a} + {b}")
    # Return
    # Once function is done running values "a" "b" returned to values
    # Values are left open for next function call to replace "a" "b"
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(17, 5)
height = subtract(60, 4)
weight = multiply(6, 20)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

# Operation moves from right to left based in function calls
what = add(age, multiply(height, subtract(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print("New Formula:")
math = multiply(weight, add(height, subtract(iq, divide(age, 3))))
print("That becomes: ", math)
# This is a test
