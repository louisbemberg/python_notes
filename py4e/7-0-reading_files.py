# standard syntax:
# variable = open(filename, mode)

file = open('./7-1-helloworld.txt')
# for line in file: # for loop on files will read line by line
#   print(line)
# counting amount of lines in a file:
count = 0
for line in file:
  count += 1
print('line count:', count)


print('where my cursor at?', file.tell())
file.seek(0) # reset cursor at 0 on file
print('where my cursor at?', file.tell())

# you can also read the content of the  file and get it as one fat string:
string_content = file.read()
print("string content:", string_content)

# how many chars in that file?
print(len(string_content))

# looking for all the lines that start with 'From:'
file.seek(0) # reset cursor at 0 on file
for line in file:
  if line.startswith('From') :
    print(line)

# if you want to get rid of extra new lines, use rstrip which will remove \n

# other approach to the loop above:
file.seek(0) # reset cursor at 0 on file
for line in file:
  if not line.startswith('From:'):
    continue # jumps to next iteration if doesnt start with from.
  print(line)

# get me all the lines with gmail addresses:
file.seek(0) # reset cursor at 0 on file
for line in file:
  if not "gmail" in line:
    continue # jumps to next iteration if doesnt start with from.
  print(line)
