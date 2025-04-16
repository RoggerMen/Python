# La función "Super()" en PYTHON
# Sirve para acceder y llamar a METODOS de la SUPER CLASE pero desde la SUBCLASE
# FACILITA la extensión de funcionalidades y acceso a METODOS de atributos de la SUPERCLASE sin tener que nombrarlas EXPLICITAMENTE lo que es especialmente util en jerarquias de CLASE COMPLEJAS

class LivingBeing:
    def __init__(self, name):
        self.name = name
        
class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        print(f"Hello! I'm a person. I'm {self.name} and I'm {self.age} years old")

class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self.student_id = student_id
            
        def greet(self):
            super().greet()
            print(f"Hello, my student ID is {self.student_id}")
            
        def introduce(self):
            print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Person("Rogger", 23)
student.greet()
student = Student("Roosvelt",23,"S123")
student.greet()
student.introduce()




