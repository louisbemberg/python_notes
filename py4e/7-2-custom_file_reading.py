filename = input('Enter the file name :')

try:
  filehandle = open(filename)
except:
  print('File cannot be opened:', filename)
  quit() # telling python to stop reading this file

count = 0
for line in filehandle:
  if '@' in line :
    count += 1
print('A total of', count, 'emails were found')
