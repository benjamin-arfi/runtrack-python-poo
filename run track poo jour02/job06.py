class Vehicule:

    def __init__(self,marque,model,annee,prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix
    
    def informationVehicule(self):
        print(self.marque , self.model , self.annee , self.prix)
    
    def demarer(self):
        print("attention je roule")

class Voiture(Vehicule):

    def __init__(self, marque ,model,annee,prix):
        Vehicule.__init__(self , marque ,model ,annee,prix )
        self.portes = 4

    def informationVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.model}")
        print(f"Annee = {self.annee}")
        print(f"Prix = {self.prix}")
        print(f"Nombre de porte = {self.portes}")
    
    def demarer(self):
        print("en voiture on y va")

class Moto(Vehicule):

    def __init__(self,marque,model,annee,prix):
        Vehicule.__init__(self,marque,model,annee,prix)
        self.roue = 2

    def informationVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.model}")
        print(f"Annee = {self.annee}")
        print(f"Prix = {self.prix}")
        print(f"Nombre de roue = {self.roue}")
    
    def demarer(self):
        print("rouler a moto vroum vroum")
    
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

voiture.demarer()
moto.demarer()
