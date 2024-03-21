
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
class ListePersonnes:

    personne_cree = 0

    def __init__(self):
        self.personnes = []

# Ajoutez une méthode ajouter_personne(nom, age) pour ajouter une nouvelle personne à la liste.
        
    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.personnes.append(nouvelle_personne)

        ListePersonnes.personne_cree += 1
        print("----------------------------------------------------------------------")
        print(f"Ajout de personne:\nNom: {nom}, age: {age}")