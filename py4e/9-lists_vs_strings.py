string = "Good Freaking Morning Team!!"
array_of_words = string.split()

print(array_of_words)

# If you want to get all the chars, need a different approach:
print(list(string)) # not sure why that works lel

# split is smart!
string2 = "Hello            World     :)"
string2.split() # ['Hello', 'World', ':)']

# split default is spaces. can be anything:
string3 = "#happy#dior#joy#instagram"
string3.split('#')

# real example:

content = "From louis.bemberg@gmail.com Tue June 15 14:07:28 2021"
# using split, try to isolate "gmail.com"
words = content.split()
email = words[1]
domain = email.split('@')[1]
print(domain)
# what if i want gmail only?
provider = domain.split('.')[0]
print(provider)
