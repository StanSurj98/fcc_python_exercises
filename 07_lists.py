# Algorithms
# set of rules and steps to solve a problem

# Data Structures
# particular way of organizing data in a computer


# What is NOT a 'Collection'?
# A single 'variable' is not enough to be a collection, as it can be reassigned its value

# What IS a Collection?
# Collections allow us to put MANY values in a single variable
# such as a 'List' (JS == Array)
print([])
print([1, 2, 3, 4])
print(['yo', 'hi', 'sup'])
print([[1, 2], [3, 4], [[5, 6], 7]]) # it can be nested

# Looking INSIDE lists using Index positions list[index]
a = ['a', 'b', 'c']
print(a[2]) # c


# Strings are !! NOT mutable !! -> must create a new string, cannot change the CONTENT of a string
fruit = 'Banana'
# fruit[0] = 'b' # WILL error as it's already an uppercase!

x = fruit.lower() # !! creates COPY !! -> the ADDRESS of the original is different!
print(x) # banana
print(fruit) # Banana -> doesn't change the original!


# ---- HOWEVER -> Lists are !! MUTABLE !! ----
# We CAN change the contents of a list directly and not make a copy!
b = [1, 2, 3, 4, 5]
b[3] = 1000
print(b) # [1, 2, 3, 1000, 5]


# ---- range() function! ----
# returns a LIST of NUMBERS ranging from ZERO and up to but NOT including the PARAMETER
print(range(5)) # [0, 1, 2, 3, 4]

people = ['Ben', 'Joe', 'Dan']
print(len(people))
print(range(len(people))) # [0, 1, 2] -> "print a range from 0 and up to the length of the list"

# range() is very useful for loops and remembering what positions we're at!
# range(len(list)) is useful cuz it gives back an array of item index positions!
for i in range(len(people)):
  person = people[i]
  print('Hey there', person + '!')

# Yes, you can write it simply like this, but just for exercise
for person in people:
  print('Sup', person + "!")