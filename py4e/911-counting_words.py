# Counting words from a sentence input by the user:

word_count = dict()
print('Enter a sentence of your choice!')
line = input('>')
words = line.split()

print('Words:', words)

for word in words :
  word_count[word] = word_count.get(word, 0) + 1
print(word_count)


# iterating through a dictionary, it's possible!

for key in word_count :
  print(key, word_count[key])

# you can also get all the keys, all the values, or both:
word_count.keys()
word_count.values()
word_count.items() # retrieved in a list, separated by commas

# you can also iterate on a dict with 2 iteration variables, representing k & v
# with the help of items()
for key,value in word_count.items() :
  print(key, value)

# LET'S DO THE SAME BUT WITH A FILE:
handle = open('9111-text.txt')
counts = dict()
for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# now let's find the biggest occurence in that dict

# teacher solution:
highest_count = None
highest_word = None
for word,count in counts.items() :
  if highest_count is None or count > highest_count:
    highest_word = word
    highest_count = count

print(highest_count, highest_word)

# Lou's solution (i miss Ruby)
highest_count = max(counts.values())
# python has no good way to retreive a key from a value.3
# we do it the hard way, so might as well go the teacher way. Doodoo python!!!
for word,count in counts.items() :
  if count == highest_count:
    highest_word = word
print(highest_count, highest_word)

for h in [1, 2, 3]:
  print(h)




