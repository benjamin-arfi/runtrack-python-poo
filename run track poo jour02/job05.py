from math import*
class Forme:
    def __init__(self):
        pass
    
    def aire(self):
        print(0)

class Rectangle(Forme):
    def __init__(self):
        Forme.__init__(self)
        self.largeur = 3
        self.hauteur = 2
    def aire(self):
        print(f"l'aire d'un rectangle longeur * largeur {self.largeur*self.hauteur} m^2")

class Cercle(Forme):
    def __init__(self):
        Forme.__init__(self)
        self.radius = 3
    
    def aire(self):
        print(f"l'aire du cercle est :{(self.radius)**2*pi} m^2")

rectangle = Rectangle()
cercle = Cercle()

rectangle.aire()
cercle.aire()