# Strings can be added. It's called concatenation
print("Hello" + " " + "World")

number = "15"

# convert a string into an integer
print(int(number) - 9)

# Strings have indexes
print("Louis"[2]) # u

# careful about reading non-existing indexes
# print("Louis"[19]) # string index out of range

# length of a string
length = len("Louis")
print(length) # 5

# looping through a string using while
fruit = 'banana'
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(index, letter)
  index = index + 1

# looping through a string using for. More elegant but no access to index
for letter in fruit:
  print(letter)

# count how many a's are in banana
count = 0
for letter in fruit:
  if letter == 'a':
    count += 1
print(count, "a's")

# chunks of strings
nickname = "louis"[0:3] # 0 up to but not including 3
nickname_v2 = "louis"[:3]

print(nickname)
print(nickname_v2)

# the in operator:
"a" in "banana" # true
"n" in "banana" # true
"nan" in "banana" # true
"bna" in "banana" # false

# evaluates alphabetical order:
print("a" > "b") # false
print("A" > "a") # false
print("zebra" > "Arantxa") # true
# a small letter will always be bigger than a big one. fuck logic
#ABCEDFGHIJKLMNOPQRSTUVWXYZabcefeghijkklmnopqrstuvwxyz
# > and < compare indexes of the order above.

# built in string methods
wzup = "WASSUPPP"
wzup.lower()
wzup # non destructive. still upcase

dir(wzup) # spits out ALL the available built-in methods.

# challenge : which email service is this customer using?
email = "louis.bemberg@gmail.com"
# first, find the index of where the @ is:
at_sign = email.find('@')
# next, look for the FIRST DOT AFTER THE @:
dot = email.find('.', at_sign) # telling python to start looking from @ onwards
# extracting gmail:
email_provider = email[at_sign + 1 : dot]
print(email_provider) # gmail

