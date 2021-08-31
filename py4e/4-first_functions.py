# function
def helloworld():
  print('Hello world!')
  print('My name is Louis!')


helloworld()
helloworld()
helloworld()

def greet(wzup):
  print("Hellloooo", wzup)

greet("Louis")


def international_greet(language):
  if language == 'fr':
    return 'bonjour'
  elif language == 'en':
    return 'hello'
  else :
    return 'hola'

print(international_greet('fr'), "World")

def add(a, b):
  return a + b

print(add(15, 6))
