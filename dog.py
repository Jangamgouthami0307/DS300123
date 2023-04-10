class Dog:
    def __init__(self, name, age):
        # : It should have a function ‘description()’ which prints the name and age of the dog.
        self.name = name
        self.age = age
 
# Create instances of our class, using our new constructor
d1 = Dog('JackRussellTerrier', 4)
d2 = Dog('Bulldog', 3)

print(d1.name, d1.age) #  JackRussellTerrier 4
print(d2.name, d2.age) # Elf 3


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# :It should have a function ‘get_info()’ which prints the coat color of the dog.
def sayHi(dog):
    print(f'Hi, my name is {dog.name} and I am {dog.age} years old!')

d1 = Dog('JackRussellTerrier', 4)
d2 = Dog('Bulldog', 3)

sayHi(d1) # Hi, my name is Dot and I am 4 years old!
sayHi(d2) # Hi, my name is Elf and I am 3 years ol

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method takes a second parameter -- times
    def bark(self, times):
        print(f'{self.name} says: {"woof!" * times}')

d = Dog('JackRussellTerrier',4)

d.bark(1) # Dot says: woof!
d.bark(4) # Dot says: woof!woof!woof!woof!# Objects are mutable so aliases change!
# !Create objects and implement the above functionalities.

import copy

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog1 = Dog('Dino', 10, 'shepherd')
dog2 = dog1            # this is an alias
dog3 = copy.copy(dog1) # this is a copy, not an alias

dog1.name = 'Spot'
print(dog2.name) # Spot (the alias changed, since it is the same object)
print(dog3.name) # Dino (the copy did not change, since it is a different object)



