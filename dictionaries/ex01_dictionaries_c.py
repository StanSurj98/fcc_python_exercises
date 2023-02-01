# Now let's put most of the things we learned together in this exercise to read a file and count the words

name = input('Enter filename:')
handle = open(name)

counts = dict()
for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1 # That pattern we keep seeing over & over - .get() used to it :P

bigcount = None
bigword = None
for word, count in counts.items():
  if bigcount is None or count > bigcount:
    # Replace the biggest counter & word at initial OR if something is more frequent
    bigcount = count
    bigword = word
print(f"Biggest word & count: {bigword, bigcount}")
