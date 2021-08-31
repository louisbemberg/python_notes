# creating a dictionary
dictionary = dict()
other_dictionary = {}

print(dictionary == other_dictionary) # true

# creating key-value pairs
dictionary['first_name'] = 'Louis'
dictionary['last_name'] = 'Bemberg'
dictionary['DOB'] = 150694

print(dictionary)


# using dictionaries to vote a color:
votes = ["red", "blue", "green", "red", "yellow", "blue","red", "red", "blue","red", "green", "blue","red", "blue", ]
colors = dict()
for color in votes :
  if color not in colors :
    colors[color] = 1
  else :
    colors[color] += 1

print(colors)

# WARNING: YOU CANNOT READ A KEY THAT DOESNT EXIST IN A DICT.
# YOU MUST PROTECT YOUR CODE BEFORE IT HAPPENS (NOT LIKE JS AND RUBY)

# important: this pattern is so common that we can use the get method:
# let's rewrite the code above:

colors = dict()
votes = ["red", "blue", "green", "red", "yellow", "blue","red", "red", "blue","red", "green", "blue","red", "blue", ]
for vote in votes :
  colors[vote] = colors.get(vote, 0) + 1
print(colors)

# We try to read the value colors[vote]. if doesn't work, assign to default 0. Otherwise, give the normal value. add 1 to that.
