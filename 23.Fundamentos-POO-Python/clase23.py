class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hola mi nombre es" , self.name, "y tengo", self.age)

person1 = Person("Rogger", 23)
person2 = Person("Mia", 21)

person1.greet()
person2.greet()



