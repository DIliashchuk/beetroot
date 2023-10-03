# Method overloading.

# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
# Also, create a simple generic function,
# which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.


class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'Woof woof'


class Cat(Animal):
    def talk(self):
        return 'Meow'


def animal_talk(animal):
    if isinstance(animal, Animal):
        return animal.talk()
    else:
        raise ValueError("Input must be an instance of Animal, Dog, or Cat")


dog = Dog()
cat = Cat()

print(animal_talk(dog))
print(animal_talk(cat))
