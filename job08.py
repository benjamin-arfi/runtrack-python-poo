class Livre:

    def __init__(self):
        self.__titre = "le medecin malgres lui"
        self.__auteur = "Moliere"
        self.__nombre_de_pages = 50
        self.__disponible = True

    def setTitre(self,titre):
        self.__titre = titre
        return self.__titre
    
    def setAuteur(self,auteur):
        self.__auteur = auteur
        return self.__auteur
    
    def setNombre_de_pages(self,nombre_de_pages):
        if nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else :
            self.__nombre_de_pages = print("erreur")
   
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur

    def getNombre_de_pages(self):
        return self.__nombre_de_pages

    def Verification(self):
        if self.__disponible == True:
            print("disponible")
            return True
        else:
            print("indisponible")
            return False

    def Emprunter(self):
        if self.Verification():
            self.__disponible = False
        else:
            print("deja emprunter")
    def rendre(self):
        if self.Emprunter():
            self.__disponible = True
        else:
            print("allez l'emprunter")


livre1 = Livre()

print(livre1.getAuteur(),livre1.getNombre_de_pages(),livre1.getTitre(),livre1.Verification())
livre1.Emprunter()
print(livre1.Verification())
livre1.rendre()
print(livre1.Verification())
