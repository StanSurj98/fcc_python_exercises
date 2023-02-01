# Finding the Largest
print('Common Loop Pattern #1 => Finding the Largest number in a list:\n')
print('1) Hold a variable for current largest number')
print('2) Check the next number in the list, if larger, replace variable -> otherwise, continue checking')
print('3) Print that current number')
print('4) Finally, return the variable which SHOULD be the largest number \n')

curr_largest = -1
print('Before Looping:', curr_largest)
for i in [1, 25, 10, 26, 86, 109, 32, 60]:
  if i > curr_largest:
    curr_largest = i
  print('Current Largest:', curr_largest, 'i:', i)
print('After Looping, Largest:', curr_largest, '\n')

# Finding the Smallest
print('Same thing but smallest instead\n')

curr_smallest = None
print('Before Looping:', curr_smallest)
for i in [99, 125, -23, 5, -83, -134, 56]:
  if curr_smallest is None:
    curr_smallest = i
  elif curr_smallest > i:
    curr_smallest = i
  print('Current Smallest:', curr_smallest, 'i:', i)
print('After Looping, Smallest:', curr_smallest, '\n')

# Note the usage of None, Is and there's another Is Not type 
# None is like Null, explicitly EMPTY
# "Is" points if it's the EXACT same thing, same address, same value, same type
# "==" only checks for same value
# "Is Not" is self-explanatory

# However...
# Don't overuse Is, only use it with booleans or None tbh (still idk if good to use for dictionaries or hashes later)


# Counting Letters
word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
count = 0
for letter in word:
  if letter == "o":
    count += 1
print('The number of "o\'s" in this word is:', count)

# len() => similar to .length() in JS
print('There are this many characters in this word:', len(word))