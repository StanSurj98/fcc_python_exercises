# Concatenate lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


# Slicing Lists using ':'
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# !! Up to but NOT including !!
print(d[2:8]) 
print(d[:6])
print(d[3:])
print(d[:])

# List Methods
x = list()
print(type(x)) # 'list'
# !! HELPFUL METHOD TO FIND ALL METHODS !!
print(dir(x))


# Building Lists from Scratch

# create an empty list
abc = []
xyz = list()
# .append() things to the list, stays in order, can be variable types
abc.append('book')
xyz.append(147)
abc.append(69)
xyz.append(['hello'])
abc.append('cookie')
print("abc:", abc, "xyz:", xyz)


# Check something IN or NOT IN a list
jkl = [1, 61, 234, 46, 82]
print(9 in jkl) # False
print(9 not in jkl) # True


# Lists are ORDERED - Can be SORTED
friends = ['Carol', 'Bob', 'Alice'] 
friends.sort()
print(friends) # !! Lists MUTABLE, changes original !! sorts by unicode values


# 'Mathy' built-in functions
nums = [4, 35, 64, 17, 0, 83]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

# Exercise for user list number and average calculator

# 1. start with empty list which will hold user input numbers
# 2. allow user to input numbers over and over until they press done - looping?
# 3. make sure user input is inside try/except and only accept numbers
# 4. append the user input to the empty list
# 5. calculate average of the final list

def avg(list_of_nums):
  return sum(list_of_nums) / len(list_of_nums)

numlist = []

while True:
  userinput = input('Enter a number: ')

  if userinput == 'done':
    break

  if not userinput.isdigit():
    print('Invalid, skipping...')
    continue

  numlist.append(float(userinput))
# f'string {code}' -> string templates in JS
print(f'From your list: {numlist}\nThe average is: {avg(numlist):.2f}') # :.2f -> limits 2 float decimal points