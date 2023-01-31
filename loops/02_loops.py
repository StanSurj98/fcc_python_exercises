# While Loops
print('While Loops => Must have base condition, "continue" goes to NEXT iteration, "break" exits loop completely \n')

def countdown(n):
  while n > 0:
    print(n)
    n -= 1
  print('Blastoff! \n')

print('This is a countdown function with a while loop')
countdown(5)


while True:
  line = input('Type "#" to skip or "done" to exit >: ')
  if line[0] == '#':
    continue # goes to next iteration INSIDE loop
  if line == 'done':
    break # exits entirely
  print(line)
print('Done! \n')

# For In... Loops
print('For In... Loops => "i" is iteration variable that goes through each items in the sequence, runs the code block for each iteration \n')
print('Counting down to sleep...')
for i in ["11:58", "11:59", "00:00", "It's midnight go to sleep!"]:
  print(i)
print('\n')


print('You can use "for in..." loops with a [list] directly OR you can store the list in a variable \n')

script = ['Obi-wan: "Hello there."', 'Grievous: "General Kenobi!!"', 'Grievous: "You are a bold one!"']
for line in script:
  print(line)





