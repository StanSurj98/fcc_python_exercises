# Variables
print('Variables => name then single "=" to assign value \n')
anything = 123
can = 'hi'
be_a = False
variable = True
print("anything =", anything)
print("can =", can)
print("be_a =", be_a)
print("variable =", variable)

print("\n")

# if, elif, else
print('Conditionals => if, elif and else statements (":" and indentation define blocks of code) \n')
a = 10
if a < 10:
  print('less than 10')
elif a == 12:
  print('exactly 12')
else:
  print('(btw! no need for else tbh...) but a is', a)

print("\n")

# try... except - try runs a code line, if breaks defaults to except and throw no errors/tracebacks
print('Try... Except => runs code that MIGHT break BUT you provide a substitute if it does')

b = 'hello'
c = 10
try:
  d = int(b) + c
except:
  d = c * 2
print('try block will fail -> "d" is going to be 20 since "hello" is a string \n')


# Functions
print('Lastly, functions are reusable code blocks, "return" is implicit last line but you can add if you want \n')
def sum(e, f):
  return e + f

print(sum(10, 5))
