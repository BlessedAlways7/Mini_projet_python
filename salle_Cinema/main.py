#from salle_Cinema.reservations import Reservations
#from salle_Cinema.salleCinema_dao import SalleCinemaDao
from reservations import Reservations
from salleCinema_dao import SalleCinemaDao

def choix_option():
      print("\n\tMenu Principal : \n"
           "\t[1] Réserver une place.\n"
           "\t[2] Afficher les places reservees.\n"
           "\t[3] Afficher les places disponibles.\n"
           "\t[4] Afficher les réservations faites par une personne spécifique.\n"
           "\t[5] Annuler réservations faites par une personne spécifique.\n"
           "\t[6] Réserver une pplace spéciale pour une personne handicapée.\n"
           "\t[7] Quitter le programme.")
      choix = input("Veuillez choisir parmi les options suivantes: ")
      return choix

choix_option()

def reserve_place():
    nom = input("Nom de la personne qui réserve une place: ")
    prenom = input("Prénom de la personne qui réserve: ")
    place = input("Nombre de place à réserver : ")
    return Reservations(nom,prenom,place)

def saisie(): 
        salleCinemaDao= SalleCinemaDao
        while True:
              choix = choix_option()
              if choix =="1":
                  nom = input("Nom de la personne qui réserve une place: ")
                  prenom = input("Prénom de la personne qui réserve: ")
                  place = input("Nombre de place à réserver : ")
                  SalleCinemaDao.reserver_place(nom, prenom,place)
                  if nom:
                    print(f"{nom} a réservé {place} place.")
                  else:
                    print("Désole, il n'y a plus de places disponibles.")

              elif choix == "2":
                  print("Les places réservées sont:")
                  SalleCinemaDao.afficher_places_reservees()

              elif choix == "3":
                  print(f"Il y a {SalleCinemaDao.places_disponibles()} places disponibles.")

              elif choix == "4":
                  nom = input("Nom de la personne qui a faite la réservations : ")
                  SalleCinemaDao.filtrer_reservations_par_personne(nom)   
                    
              elif choix == "5":
                  nom = input("Nom de la personne pour annuler les réservations : ")
                  SalleCinemaDao.annuler_reservation(nom)

              elif choix == "6":
                  nom = input("Nom de la personne pour laquelle il faut réserver une place spéciale: ")
                  SalleCinemaDao.reserver_place_speciale(nom)

              elif choix == "7":
                  print("Au revoir!")
                  break
              else:
                  print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 et 7.")
               
saisie()           