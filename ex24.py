print("Let's practice everything.")
print('You\d need to know \ bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe kitty is so sweet
The kitty is so nice
\n\t\tI love the kitty.
"""
print("-----")
print(poem)
print("-----")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(monster):
    kitty_paws = monster * 50
    kitty_ears = kitty_paws / 25
    kitty_nose = kitty_ears / 12
    return kitty_paws, kitty_ears, kitty_nose


start_point = 125
paws, ears, nose = secret_formula(start_point)

# Another way to format a string
print("With a basket of {} kitens.".format(start_point))
print(f"We'd have {paws} paws, {ears} ears, and {nose} noses.")
print('What happened to the kitties? TTT^TTT')

start_point = start_point / 10

print("We can also do that this way: ")
formula = secret_formula(start_point)
print("We'd have {} paws, {} ears, and {} noses.".format(*formula))
