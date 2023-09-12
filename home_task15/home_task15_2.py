class Dog:
    age_factor = 7  # Class attribute

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

dog = Dog(3)
human_equivalent_age = dog.human_age()
print(f"The dog's human equivalent age is {human_equivalent_age} years")
