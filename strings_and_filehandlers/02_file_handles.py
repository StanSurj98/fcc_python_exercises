# Handle -> Such as when reading a file on a computer 

# open() -> similar to fs() in JS library, it opens and reads a particular file, but doesn't return the ENTIRE file
# fhand = open('text.txt') # this doesn't exist so it'll break

# The '\n' newline character
str = 'hello\nworld'
# this prints hello
#             world
print(str)
abc = 'a\nb\nc'
print("Length of abc including special chars:", len(abc)) # You'd think it's 3, but it's 5. \n counts as a char length and has index
print(abc[1]) # just prints the newline on the screen

# Why is this important?

# Suppose you have a text file like this

# Hello world
# how are you today
# I am a coding file 
# that does nothing

# This is TECHNICALLY 

# Hello world\n
# how are you today\n
# I am a coding file\n
# that does nothing\n

# How do we read that line by line?
fhand = open('sample.txt')
print(fhand) # This returns a python handle for the file, but it's a !! SEQUENCE !! aka an ordered set, we can LOOP thru it

for line in fhand:
  print(line) # we can literally get back each line!

# What if we want to COUNT the lines?
sample = open('sample.txt')
count = 0
for line in sample:
  count += 1
print("Line Count:", count)

# Reading ENTIRE files -> .read() returns the entire file in one long string and includes the '\n' chars
thand = open('sample.txt')
text = thand.read()
print(text)
print(text[:5]) # You can then use any string methods you want on the entire file!
print(text[:5].upper()) # 'HELLO'