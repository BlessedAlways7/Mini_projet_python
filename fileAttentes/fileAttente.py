# Création de la classe File Attente avec les attributs.
class FileAttente:
    def __init__(self, nom, prenom, age, prioritaire):
        self.__nom = nom
        self.__prenom = prenom
        self.age = age
        self.prioritaire = prioritaire

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def get_prioritaire(self):
        return self.prioritaire

    def set_prioritaire(self, value):
        self.prioritaire = value


