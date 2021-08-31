n = 0

while n <= 18 :
  print('one year passes! Happy birthday!')
  n = n + 1
print('you are 19 years old. :)')
print(n)

i = 5
while i > 6 :
  print('this loop gets completely ignored')


# you can manipulate the flow of a loop with break and continue:

while True:
  user_input = input('> ')
  if user_input[0] == '#' :
    continue # jumps to the next loop without reading rest of block.
  if user_input == 'quit' :
    break
  print(user_input)
print('finished!')

# the closest you'll ever get to ruby's each!
for i in ['John', 'Ringo', 'Paul', 'George'] :
  print(i)
print('the beatles!!!')

# finding the smallest number in a list
smallest = None # none is a constant therefore capital. like nil.
print('before')
for value in [3, 8, 2, 4, 9] :
  if smallest is None : # 'is' is a stricter ==
    smallest = value
  elif value < smallest :
    smallest = value
print('After', smallest)
