class PartyAnimal:
  x = 0

  def __init__(self): # constructor
    print('You just ran the constructor!')

  def __del__(self): # delete
    print('Successfully deleted', self)

  def party(self):
    self.x = self.x + 1
    print("So far", self.x)

  def scream(self): # must always receive self as first param
    print("Woohoo!")


# creating a PartyAnimal instance:
party_animal1 = PartyAnimal()
party_animal2 = PartyAnimal()

print(type(party_animal1)) # <class '__main__.PartyAnimal'>

party_animal1.scream() # prints "Woohoo"

print(dir(party_animal1)) # tells you all the available methods

party_animal1.__del__ # one way to delete an object
party_animal2 = "something else haha" # reassigning the variable also deletes it!
print(party_animal1)


class PartyFreak(PartyAnimal): # PartyFreak Inherits from PartyAnimal
  y = 10

party_freak1 = PartyFreak()

print(party_freak1.x, party_freak1.y)
