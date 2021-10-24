import string
import itertools

file = open("jackbox_codes.txt", "w")

all_combos = [''.join(x) for x in itertools.product(string.ascii_uppercase, repeat=4)]

for x in all_combos:
    file.write(x + "\n")