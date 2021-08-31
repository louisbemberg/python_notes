handle = open('9130-blabla.txt')
counts = dict()

for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts) # all the words and their count

tmp = list()
for key, val in counts.items():
  tmp.append((val, key))

print(tmp) # keys and values have been flipped
ranking = sorted(tmp, reverse=True)
top10 = ranking[0:10]

for v, k in top10:
  print(k, '=>', v)

## MUCH SHORTER REFACTORED VERSION:

# imagine we got the following dict
dic = {'Louis': 27, 'JC': 69, 'Pauli': 28, 'Sash': 26}

# the stuff inside [] is a comprehension: instructions on how to manufacture the content of a list with a function.
sorted_by_values = sorted([ (v,k) for k,v in dic.items()])

print('sorted in one line:', sorted_by_values)
