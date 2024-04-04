class Reservations:
    def __init__(self,nom,prenom, place) -> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__place= place

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
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

        