class Personne:
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print(self.age)
    
    def bonjour(self):
        print("hello")
    
    def modifierAge(set,age):
        self.age = age
        return self.age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("je vais en cours")

    def affichageAge(self):
        print(f"j'ai {self.age} ans")

class Professeur:
    def __init__(self):
        self.__matiereEnseignee = "math"

    def enseigner(self):
        print(f"le cours de {self.__matiereEnseignee} va commencer ")

Personne1 = Personne()
eleve1 = Eleve()
eleve1.affichageAge()