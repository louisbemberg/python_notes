for i in [5, 4, 3, 2, 1]:
  print(i)
print('go!')

beatles = ['John', 'Paul', 'George', 'Ringo']
for beatle in beatles:
  print(beatle, 'sings!')

zero_to_three = range(4)

for i in zero_to_three:
  print(i)

# keeping track of i instead of beatle
for i in range(len(beatles)):
  print(i, beatles[i])

# adding lists
[1, 2, 3, 4, 5, 6] == [1, 2, 3] + [4, 5, 6] #true

fruits = ['apple', 'pear', 'orange', 'mango', 'kiwi', 'banana', 'coconut', 'peach']
fruits[0:2] == fruits[:2]#['apple', 'pear']
print("two by two:", fruits[0:6:2]) # ["apple", "orange", "kiwi"] start at 0, stop at 6 (non inclusive), select every 3rd one.

print(fruits[2:5]) #['orange', 'mango', 'kiwi']

# reversing the array:
reversed_fruits = fruits[::-1]

# two ways to get all the fruits
fruits == fruits[:]

#creating empty lists:

x = list()
y = []

print(x == y) # True

# adding things to a list:
numlist = list()
numlist.append(15)
numlist.append(6)
numlist.append(8)
numlist.append(2)

# calculating the average:
average = sum(numlist) / len(numlist)

# equivalent of each_with_index
golfers = ["Tiger Woods", "Phil", "JT", "Spieth", "Schauffle", "DJ"]
for i, golfer in enumerate(golfers):
  print(i, golfer)





