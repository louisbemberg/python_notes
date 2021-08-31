# printing to the screen
print('Hello world')

# input and interpolating it
answer = input("What's your name?\n")
# format string
print(f"Well hello {answer}!")

x = 6
y = 15
if (x < y):
    print(f'{x} is smaller than {y}!')
else:
    print(f'{x} is smaller than {y}!')


# coughing three times:
i = 3
while i > 0:
    print('Cough!')
    i -= 1

# coughing three more times:
for k in [0, 1, 2]:
    print("cough")

# coughing n times:
n = 7
for p in range(n):
    print('COUGH')


# some ranges:
print(list(range(15))) # from 0 to 14
print(list(range(5,10))) # from 5 to 9
print(list(range(5, 75, 5))) # from 5 to 70, increments of 5

# How to make range inclusive?
def range_inclusive(start, end, incr = 1):
    return range(start, end+incr, incr)

print(list(range_inclusive(5,75,5)))
print(list(range_inclusive(5,10)))

# some definitions

# range - sequence of numbers
# list - sequence of mutable values
# tuple - sequence of immutable values
# dict - collection of key-value pairs
# set - collection of unique values

words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, 'r')
    for line in file:
        words.add(line.rstrip('\n'))
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True


# agreements 

answer = input("Do you agree? \n")

if answer.lower() in ["y", "yes", "yeah", "yup", "ye"]:
    print("Agreed")
else:
    print('Not agreed.')


# swapping values
x = "Louis"
y = "Bemberg"

x, y = y, x

print(x) # Bemberg
print(y) # Louis

import csv

file = open('filename.csv', 'a')
name = input("Name: ")
number = input("number: ")
writer = csv.writer(file)
writer.writerow((name, number))
file.close()

# block above refactored: 
with open('filename.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow((name, number))


# regex

import re

s = input('Do you agree? \n')

if re.search("y(es)?", s, re.IGNORECASE):
    print('Agreed')
if re.search("n(o)?", s):
    print('Not Agreed')


    