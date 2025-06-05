class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")

# INHERITANCE IS WHEN YOU MAKE A CLASS A PARAMETER IN ANOTHER CLASS IF YOU WANT TO INHERIT 
# A FUCTION FROM THAT CLASS

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
