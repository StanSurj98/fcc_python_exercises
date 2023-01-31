# Let's kick it up a notch with file openings

# Note! '\n' counts as a char, AND it counts as a whitespace
# Also print() adds a '\n' to the end of it, so usually we will print each line as a double space
# So let's say we want to print out all the contents of a file, but without double spacing it

fhand = open('sample_text_2.txt')
for line in fhand:
  line = line.rstrip() # Get's rid of the '\n' at the end and prevents double space
  if line.startswith('From:'):
    print(line) # Can write as -> print(line.rstrip())


# What if we give the option to the user which file to open?
fname = input('Enter Filename to Open: ')
# fhand = open(fname) # !! this might break !! what if user inputs bad stuff? bad names? etc? 
try:
  fhand = open(fname)
except:
  print('Sorry the filename: "', fname, '" does not exist')
  quit() # !! VERY IMPORTANT !! to quit here, otherwise code below this keeps going and tracebacks

for line in fhand:
  line = line.rstrip()
  if not line.startswith('From:'): # NOT operator => "If the line does NOT startwith 'From:' "
    continue # similar to code above, we will skip all lines that do not start with "From:"
  print(line) # else, just print the line (again omit else cuz we can)



# Similar but this time we're looking to print all lines containing substring 'hello' ONLY
f2name = input('Enter Filename to Open: ')
try:
  f2hand = open(f2name)
except:
  print('Sorry the filename: "', fname, '" does not exist')
  quit() # !! VERY IMPORTANT !! to quit here, otherwise code below this keeps going and tracebacks


for line in f2hand:
  line = line.rstrip()
  if not 'hello' in line: 
    continue # again... "if 'hello' is NOT in the line, skip and continue the iteration"
  print(line)