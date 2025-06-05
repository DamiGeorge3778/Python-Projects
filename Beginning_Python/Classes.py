import random
# class Mammal:
#     def eat(self):
#         print("eat")
#     def walk(self):
#         print("walk")

# m = Mammal()
# m.eat()

# SIMPLE EXAMPLE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# create classes
class Pet1:
    def dog(self):
        print("Woof! Woof!")
class Pet2:
    def cat(self):
        print("Meow! Meow!")
class Pet3:
    def bird(self):
        print("Caw! Caw!")
# store class references in a list
pet_classes = [Pet1, Pet2, Pet3]
# select random class and create an instance
pet_instance = random.choice(pet_classes)()
# call appropriate method dynamically/create instances
if isinstance(pet_instance, Pet1):
    pet_instance.dog()

elif isinstance(pet_instance, Pet2):
    pet_instance.cat()

elif isinstance(pet_instance, Pet3):
    pet_instance.bird()


