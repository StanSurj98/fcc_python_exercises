# Lists are ordered items
# Dictionaries are like a BAG of values each with its own label - no intrinsic order

# Synonyms in other Languages
# Associative Arrays - Perl/PHP
# Properties or Map or HashMap - Java
# Property Bag - C#/.NET
# Objects - JS

# We 'index' things in Dictionaries using their label tags (keys)
list_ex = [0, 1, 2, 3, 4, 5]
print(f"Original List: {list_ex}")
list_ex[2] # 2
list_ex[2] = 100 # we can reassign them at position - [0, 1, 100, 3, 4, 5]
list_ex[len(list_ex) - 1] = 5 * 22 # call methods inside index and then reassign with an operation performed as well
list_ex.append(6)
print(f"New list: {list_ex}")


# Can use dict() constructor for a dictionary
purse = dict()
purse['money'] = 100
purse['keys'] = "jingle jingle"
purse['tissue'] = None
print(purse)
print(f"If we wanna know how much money: {purse['money']}")
purse['money'] = purse['money'] + 50 # can reassign or update
purse['tissue'] = 'ACHOOO!'
print(f"After our modifications: {purse}")

# Dictionary Literals similar to lists
lst = [0, 1, 2, 3]
dct = {"hi": 1, "there": 2, "everyone": 3}
numkeys = {0: "the", 1: "keys", 2: "are", 3:"numbers!"}

# Can use a list as indices to access a dictionary
for i in lst:
  print(f"The word at numkeys[{i}] is: {numkeys[i]}")
