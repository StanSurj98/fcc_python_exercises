# Strings are more in depth in Python vs JS

# Slicing Strings

# Everything is still 0 indexed
s = "Monty Python"
# s[start : up-to but NOT include this index]
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[4:100]) # Python - Notice! No traceback here, it doesn't care if you go over len(s)

# You can Omit left or right side
print(s[:2]) # Mo -> "go from start, up to but not including index '2' "
print(s[8:]) # thon -> "start from index 8, go til the end"
print(s[:]) # Monty Python -> print the entire thing


# 'in' as a LOGICAL operator, NOT as "for loop"
fruit = 'banana'
# It implicitly returns True/False, but here we'll do a print() if true
if 'a' in fruit:
  print(True) # True

if 'm' in fruit:
  print(True)
else:
  print(False) # False

if 'nan' in fruit:
  print('Yup!') # Doesn't need to be 1 char


# String Methods -> a TON more in Python docs btw...

# .lower() -> same to JS, RETURNS A NEW STRING! Does NOT modify original!
b = 'Hello World'
lowered = b.lower()
print(lowered) # 'hello world'

# .upper() -> can also type string directly into arg
print('hello world'.upper()) # 'HELLO WORLD'
print(b) # 'Hello World'

# .capitalize() -> capitalizes the first letter of the ENTIRE string, NOT each word
c = 'bungo stray dogs'
print(c.capitalize())


# .find(value, start, end) -> finds substring WITHIN a string, gives back index of FIRST character that matches the substring
print(c.find("o")) # 4
print(c.find('ray')) # 8
print(c[c.find('dogs')]) # d -> it's saying what is the LETTER at the INDEX returned when finding the substring 'dogs'
print(c[c.find('go'):]) # 'ungo stray dogs' -> print the entire string AFTER the index where 'go' is


# .replace() -> SEARCH and REPLACE the word with the argument passed
greet = 'Hello Alice'
print(greet.replace('Alice', 'Bob')) # 'Hello Bob'
print(greet.replace('alice', 'Bob')) # 'Hello Alice' -> !! case sensitive !!
print(greet.replace('samuel', 'Bob')) # 'Hello Alice' -> !! must match !!
print(greet) # 'Hello Alice' -> !! does not mutate original !!

# As usual you can store all of these expressions into variables
zstr = greet.replace('e', 'z')
print(zstr) # "Hzllo Alicz" -> yup you can replace all occurences of a char


# Stripping White Spaces

# .strip() .lstrip() .rstrip() -> yup python can distinguish which side
asdf = '  welcome to the jungle  '
left_strip = asdf.lstrip()
right_strip = asdf.rstrip()
both_strip = asdf.strip()
print(left_strip)
print(right_strip)
print(both_strip)
print(asdf) # !! doesn't mutate !!


# .startswith() -> checks if substring is present as first word
script = 'General Kenobi!'
print(script.startswith('General')) # True
print(script.startswith('general')) # False => !! case sensitive !!
print(script.startswith('G')) # True
print(script.startswith('g')) # False => !! case sensitive !!

# .endswih() -> same thing
print(script.endswith("obi!"))



# Exercise - Find the Email Provider
data = 'From alicebobson@icloud.ca Sat Jan 5, 2000'
# 1. use .find("@") to get its index
# 2. find where @icloud.ca ends -> finding the whitespace AFTER it
  # use the @ position for our starting slice point
  # .find(value, start) -> returns to us the whitespace index AFTER the @ sign
# 3. print the contents between atpos and wspos .find(data[atpos + 1 : wspos])

atpos = data.find('@')
wspos = data.find(" ", atpos) # "find a white space, starting from the @ index, and search until the end"
host = data[atpos + 1 : wspos] # print the substring starting from @ index until the first whitespace encountered
print("The email provider for this example is:", host)