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