# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

# add this line to use Regex:
import re

# simpler "from:" search using regex
handle = open('9130-blabla.txt')
for line in handle:
  line = line.rstrip()
  if re.search('^Lorem', line):
    print(line)


# finding all the numbers in a string:
string = "My 2 favourite numbers are 15 and 6"
y = re.findall('[0-9]+', string)
print(y) # ['2', '15', '6']

# warning: greedy matching
other_string = "From: Louis Bemberg  Received at: 15:06"
z = re.findall('^F.+:', other_string) # What do you expect this to return?
print(z) # ['From: Louis Bemberg  Received at: 15:']

# Regexp will always find the BIGGEST POSSIBLE string matching the expression.
# you can override non-greedy with a question mark:
z = re.findall('^F.+?:', other_string) # What do you expect this to return?
print(z) # ['From:']

# Let's extract "gmail" from the following string:
content = "From: louis.bemberg@gmail.com Thu 17 June 17:43:28 2021"
match_data = re.findall('^From: .*@([^ ]*)', content)
print(match_data) # ['gmail.com']
