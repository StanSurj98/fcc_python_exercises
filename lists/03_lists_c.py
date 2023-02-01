abc = "with three words"
splitted = abc.split() # "Find the whitespaces and break apart the words into a list"
print(f"Original: {abc} \nSplitted List: {splitted}")
print(f"Length of splitted list: {len(splitted)}")
print(f"Word at index 1: {splitted[1]}")

# Loop through the new list of strings
for w in splitted: 
  print(w)


line = "a lot of                       spaces"
xyz = line.split() # will ignore the multiple spaces and treat as 1
print(f"Notice the spaces are just normal?: {xyz}")
line = "first;second;third"
xyz = line.split() # here there are no whitespaces...
print(f"No whitespaces: {line} splits into: {xyz}")
thing = line.split(";") # specifying a char is called "DELIMITER"
print(f"Split at each ; however... gives us: {thing}")


# Let's try another email exercise with opening a file
fhand = open("email.txt")
for line in fhand:
  line = line.strip()
  if not line.startswith("From "): continue
  words = line.split()
  daySent = words[2]
  print(f"Day sent was: {daySent}") 


line = "From testeremail.fakelastname@googly.test.ca Sat Jan 5 09:14:15 2023"
words = line.split()
email = words[1]
pieces = email.split("@")
host = pieces[1]
print(f"Email provider is: {host}")
