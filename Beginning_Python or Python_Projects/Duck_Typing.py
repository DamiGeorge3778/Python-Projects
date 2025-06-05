class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"

class Person:
    def speak(self):
        return "Hello!"

# Duck typing in action
def make_speak(entity):
    return entity.speak()  # As long as `entity` has a `speak` method, it will work

entities = [Dog(), Cat(), Person()]
for entity in entities:
    print(make_speak(entity))  # Output: Bark! Meow! Hello!



# Without duck typing


# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Dog(Animal):
#     def speak(self):
#         return "Bark!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# class Person(Animal):  # Explicitly inheriting from Animal
#     def speak(self):
#         return "Hello!"

# # Function now requires objects to be instances of Animal
# def make_speak(entity: Animal):
#     return entity.speak()

# entities = [Dog(), Cat(), Person()]
# for entity in entities:
#     print(make_speak(entity))  # Output: Bark! Meow! Hello!