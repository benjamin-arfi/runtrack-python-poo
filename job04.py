class Personne:

    def __init__(self,nomchoisi,prenomchoisi):
        self.nom = nomchoisi
        self.prenom = prenomchoisi

    def sePresenter(self):
        return f"je suis {self.prenom} {self.nom}"

personne1 = Personne("doe", "john")
personne2 = Personne("Dupond", "Jean")

print(personne1.sePresenter())
print(personne2.sePresenter())
   
    