# Created a variable called 'formatter' w/ open format symbols
formatter = "{} {} {} {}"

# Formatting variables (W, X, Y, Z) into 'formatter' string
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))

# printing 'formatter' formatting strings (W, X, Y, Z)
# Extended '.format()' to containt multiple strings in block
print(formatter.format(
    "\n\tTry your",
    "\n\tOwn text here",
    "\n\tMaybe a poem?",
    "\n\tOr a song about Scooby Doo?"
))
