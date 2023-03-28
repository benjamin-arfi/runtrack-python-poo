class Student:

    def __init__(self,nom,prenom,numero_etudiant):
        self.__nom = nom 
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nombre_credit = 0
        self.__level 

    def setAdd_credit(self,nombre_credit):
        if nombre_credit > 0:
            self.__nombre_credit = nombre_credit + self.__nombre_credit

    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getNumero_etudiant(self):
        return self.__numero_etudiant
    def getNombres_credit(self):
        return self.__nombre_credit

etudiant = Student("Doe", "john", 145)
etudiant.setAdd_credit(10)
etudiant.setAdd_credit(10)
etudiant.setAdd_credit(10)
print(f"le nombre de credit de {etudiant.getPrenom()} {etudiant.getNom()} est de {etudiant.getNombres_credit()} points")