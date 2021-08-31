sports = ('golf', 'basketball', 'football', 'baseball')
golf = sports[0]

# tuples cannot be altered
try:
  sports[2] = 'soccer'
except:
  print('nope. cant change tuples mate.')

# you can't sort, reverse, append, etc.
# tupples are best when you just need to store some things and DASSIT
# much more limited, but much more eficient than lists.


# use tuples to assing several variables:

(x, y) = 15, 6
print('day:', x)
print('month:', y)

# remember dictionaries? using the method items() returns tuples:
d = { "name": "Louis", "last_name": "Bemberg", "age": 27, "language": "Python"}
items = d.items()
print(items)

# we are able to iterate over K & V thanks to those tuples:
for key, value in items:
  print(key, ' ==> ', value)

# when comparing tuples, it works like strings. only the first is checked unless more is needed:

(0, 45) < (1, 2) # true
(1, 2, 3) < (1, 7, 13) # true
(1, 2, "a") > (1, 2, "A") # true

# sorting a list of tuples:
d2 = { 'b': 15, 'a': 42, 'c': 27 }
sorted_items = sorted(d2.items())
print(sorted_items) # [('a', 42), ('b', 15), ('c', 27)] prints the items according to keys.

# What about sorting by values???
d3 = { 'a': 42, 'b': 15, 'c': 27 }
# we'll need the end of a temporary list.
tmp = list()
# let's iterate over d3 without doing any sorting:
for key, value in d3.items():
  tmp.append((value, key)) # we add a tuple to that list
# let's check:
print(tmp)
# now we can sort, descending:
tmp = sorted(tmp, reverse=True)
# let's recheck:
print(tmp) # [(42, 'a'), (27, 'c'), (15, 'b')]
print(dict(tmp)) # we're allowed to convert back into dict. shit's flipped tho.

