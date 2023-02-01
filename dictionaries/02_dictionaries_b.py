# Dictionaries are great for Histograms or keeping Tallies

# for example counting occurences of names
names = ["Alice", "Bob", "Carol", "Alice", "Bob", "Dan", "Edna", "Edna", "Jeff", "Jeff", "Carol", "Bob"]
count = dict()

# Common traceback is if the key doesn't exist inside the dictionary
# count['bob'] -> won't work

for name in names:
  # we can instead use the in / not in operators to check
  if name not in count:
    count[name] = 1
  else:
    count[name] = count[name] + 1
print(f"Total names: {count}")



# !! COMMON PATTERN !!

# "Retrieve if exists or set default value" is such a common pattern...
# if name in count: 
#   x = count[name]
# else: 
#   x = 0

# There is a built in dictionary method .get(key?, default_if_not)!
newTally = {}
for name in names:
  # reassign count[name] to +1 its value if exists, OR set default to 0, then + 1 the first time we encounter it
  newTally[name] = newTally.get(name, 0) + 1
print(f"Same but with .get(): {newTally}")
