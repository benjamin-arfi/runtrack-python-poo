class Animal:

    def __init__(self):
        self.age = 0 
        self.prenom = ""

    def viellir(self):
        self.age = +1
        return f"l'age de l'animal {self.age} ans"
    def nommer(self,prenom):
        self.prenom = prenom
        return f"l'animal se nomme {prenom}"

animal0 = Animal()
animal1 = Animal()

print(f"l'age de l'animal {animal0.age} ans")
print(animal1.viellir())
print(animal0.nommer("Luna"))