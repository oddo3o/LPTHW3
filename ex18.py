def print_two(*args):
    # * pulls all arguments to the function into a list
    # 'args' is being unpacked into 'arg1' and 'arg2'
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# This one is like your scripts with argv


def print_two_again(arg1, arg2):
    # 'arg' values in parentheses adds them to the function
    print(f"arg1: {arg1}, arg2: {arg2}")
# That *args is actually pointless, we can just do this


def print_one(arg1):
    print(f"arg1: {arg1}")
# This just takes one argument


def print_none():
    print("I got nothing")
# This one takes no arguments


print_two("Christian", "General")
print_two_again("Hello", "World")
print_one("First")
print_none()
