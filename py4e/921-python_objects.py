class Dog:

  def __init__(self, breed, gender, age):
    self.age = age
    self.breed = breed
    self.gender = gender

dog1 = Dog("border collie", 'female', 14)

print('A', dog1.age, 'year-old', dog1.gender, dog1.breed, '.')

# IMPORTANT
# in dog.age, the  "." is the OBJECT LOOKUP OPERATOR :)
