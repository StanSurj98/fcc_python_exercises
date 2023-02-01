# Tuples are like Lists -> have elems and 0-indexed but with (soft brackets) 
x = ('Glenn', 'Sally', 'Joseph')
print(f"Indices work: x = {x} | x[2] = {x[2]}")

y = (1, 9, 2)
print(f"Methods too: y = {y} | max(y) = {max(y)}")

print("And can loop through tuples:")
for i in y:
  print(i)

# BUT... it's IMMUTABLE -> you CANNOT change its contents
x = [9, 8, 7] # this works because we reassign the entire variable of x...
print(f"\nOriginal List: {x}")
x[2] = 1337 # BEFORE reassigning an item inside
print(f"Mutated List:{x}")

y = "ABC"
# y[2] = "D" # This tracebacks cuz we're mutating a string

z = (5, 4, 3)
# z[2] = 0 # Same here, the tuple behaves like the string and cannot be mutated

# Reason? it's more efficient vs lists -> only use Tuples if you just want to store a list but not modify it
# Better memory use & performance


# !! Things NOT to do with Tuples !! -> all these are tracebacks, they only have 2 methods
# z.sort()
# z.append(5)
# z.reverse()
l = list()
print(f"\nMethods available for a list:\n{dir(l)}") # ignore the __verb__
t = tuple()
print(f"\nMethods available for a tuple:\n{dir(t)}") # only 'count' and 'index'


# Tuple Assignment
(a, b, c) = (1, True, False) # can assign tuples on left hand side to corresponding values
d, e, f = None, "Hello there", ("world!", "Nested tuples!") # can omit the ()

print(f"\na:{a}, b:{b}, c:{c}, d:{d}, e:{e}, f:{f}") # each thing MUST be a variable though


# Tuples & Dictionaries!
d = dict()
d['yo'] = 2
d['hey'] = 3
print("\nLoopin' Tups!")
for k,v in d.items():
  print(k, v)

tups = d.items()
print(tups)

# Tuples are comparable
# operators work on tuples BUT it only checks the first and doesn't move on if it's resolved
  # UNLESS the first values are equal, then it moves to the next in the tuple, and so on... until it finds a resolution
  # Just like comparing strings - it looks at unicode values to compare each char too

print((1, 2, 3) < (4, 5, 6)) # True
print((0, 1, 20000) < (0, 3, 4)) # True - though 0 is equal, 1 < 3
print(('Jones', "Sally") < ("Jones", 'Sam')) # True - again, moves on to Sam and compares unicode
print(('Jones', 'Sally') > ('Adams', 'Sam')) # True - J > A

