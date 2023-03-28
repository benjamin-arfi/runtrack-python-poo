class Rectangle:

    def __init__(self):
        self.__longeur = 10
        self.__largeur = 5

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

rectangle1 = Rectangle()

print(rectangle1.getlongeur(), rectangle1.getlargeur())
rectangle1.setlargeur(2)
rectangle1.setlongeur(6)
print(rectangle1.getlongeur(), rectangle1.getlargeur())

