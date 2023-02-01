# Concatenate lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"concatenating a:{a} and b:{b} becomes c: {c}")


# Slicing Lists using ':'
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# !! Up to but NOT including !!
print(d[2:8]) 
print(d[:6])
print(d[3:])
print(d[:])

# List Methods
x = list()
print(type(x)) # <class 'list'>
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
print(f"Original: {friends}")
friends.sort()
print(f"Friends sorted: {friends}") # !! Lists MUTABLE, changes original !! sorts by unicode values
print(f"Collections are mutable!! Original no longer exists: {friends}")


# 'Mathy' built-in functions
nums = [4, 35, 64, 17, 0, 83]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

