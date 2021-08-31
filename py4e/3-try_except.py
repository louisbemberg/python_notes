user_input = "Hola"

# Try & except allows you to write crashing code than can be rescued.
try : # try: also works
  result = user_input + 4
except : # except: also works
  print("You were supposed to give an integer input, dumass")


# writing this code outside of try/except crashes the code:
# "Hello" / 7 #code crashes on line 11, cant divide a string by 7

# QUIZ : What will we see on screen?

try :
  print("Coucou!")
  "Je peux pas diviser une string:" / 8
  print("Bonjour!") # this line gets ignored
except :
  print ("Hello there!")
