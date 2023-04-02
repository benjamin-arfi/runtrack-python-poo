class Rectangle:

    def __init__(self):
        self.__longeur = 12
        self.__largeur = 5
    
    def perimetreR(self):
        print(f"le perimetre du rectangle est {(self.__longeur + self.__largeur)*2} m ")

    def surfaceR(self):
        print(f"la surface du rectangle est {self.__largeur * self.__longeur} m^2")
    
    def setlongeur(self,longeur):
        self.__longeur = longeur
        return self.__longeur
    
    def setlargeur(self,largeur):
        self.__largeur = largeur
        return self.__largeur
    def getlongeur(self):
        return self.__longeur
    def getlargeur(self):
        return self.__largeur
class Parallelepipede(Rectangle):

    def __init__(self):
        Rectangle.__init__(self)
        self.hauteur = 3

    def vollume(self):
        print(f"le vollume du parallelepipede rectangle est {self.getlongeur()*self.getlargeur()*self.hauteur} m^3")

rectangle = Rectangle()
parallelepipede = Parallelepipede()

rectangle.perimetreR()
rectangle.surfaceR()

parallelepipede.vollume()
