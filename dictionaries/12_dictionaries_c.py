# Let's do our common count pattern again with an input

counts = dict()
print(f"Enter a line of text: ")
line = input(">")
words = line.split()

for word in words:
  # .get(key_if_true, default_if_false)
  counts[word] = counts.get(word, 0) + 1;
print(f"Counts: {counts}")


# Definite Loops & Dictionaries
# can loop through the ENTRIES in a dictionary in order & look up the values
counts = {'chuck': 1, "fred": 42, "jan": 100}
for key in counts:
  print(key, counts[key])

# Retrieve Lists of Keys, Values or BOTH!
ccc = {'alice':100, 'bob':200, 'carol':300}
print(f"\noriginal: {ccc}")
print(f"can turn dictionary keys into list with list(dict): {list(ccc)}")
print(f"similarly with .keys(): {ccc.keys()}")
print(f"or the values only with .values(): {ccc.values()}")
print(f"or BOTH in 'tuples' with .items(): {ccc.items()}")

print("\nTwo Iteration Variables - loop tuples at once:")

# !! Two Iteration Variables !! -> Loop through a dictionary.items() and INSTANTLY get the tuples back
for aaa,bbb in ccc.items():
  print(aaa, bbb)