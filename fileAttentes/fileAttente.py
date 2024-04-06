class FileAttente:
    def __init__(self, nom, prenom,  prioritaire):
        self.__nom = nom
        self.__prenom = prenom
        
        self.__prioritaire = prioritaire


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

    @property
    def prioritaire(self):
        return self.__prioritaire

    @prioritaire.setter
    def prioritaire(self, value):
        self.__prioritaire = value

   



   

