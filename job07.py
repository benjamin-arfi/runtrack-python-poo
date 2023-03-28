class Livre:

    def __init__(self):
        self.__titre = "le medecin malgres lui"
        self.__auteur = "Moliere"
        self.__nombre_de_pages = 50

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

livre1 = Livre()

print(livre1.getAuteur(),livre1.getNombre_de_pages(),livre1.getTitre())

livre1.setAuteur("renard")
livre1.setTitre("le loup et le renard")
livre1.setNombre_de_pages(-20)

print(livre1.getAuteur(),livre1.getNombre_de_pages(),livre1.getTitre())