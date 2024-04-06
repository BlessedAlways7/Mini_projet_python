#from salle_Cinema.reservations import Reservations
#from salle_Cinema.salleCinema_dao import SalleCinemaDao
from reservations import Reservations
from salleCinema_dao import SalleCinemaDao

def choix_option():
      print("\n\tMenu Principal : \n"
           "\t[12] Réserver une place.\n"
           "\t[13] Réserver une place spéciale pour une personne handicapée.\n"
           "\t[14] Afficher les réservations.\n"
           "\t[15] Afficher les places disponibles.\n"
           "\t[16] Filtrer les réservations faites par une personne.\n"
           "\t[17] Annuler réservations faites par une personne.\n"
           "\t[18] Quitter le programme.\n")
      

def saisie(): 
        salleCinemaDao= SalleCinemaDao
        while True:
            choix = choix_option()
            choix = input("Veuillez choisir parmi les options suivantes: ")

            if choix =="12":
                nom = input("Nom de la personne qui réserve une place: ")
                prenom = input("Prénom de la personne qui réserve: ")
                place = input("Nombre de place à réserver : ")
                
                SalleCinemaDao.reserver_place(nom, prenom, place)
                print(f"{nom} a été ajouté à la réservation avec succès.")

            elif choix == "13":
                nom = input("Nom de la personne pour laquelle il faut réserver une place spéciale: ")
                prenom = input("Prénom de la personne pour laquelle il faut réserver une place spéciale: ")
                place_speciale = input("Nombre de place spéciale à réservé : ")
                print(SalleCinemaDao.reserver_place_speciale(nom,prenom, place_speciale))   
                    

            elif choix == "14":
                message, reservations = SalleCinemaDao.afficher_places_reservees()
                if reservations:
                    print(message)
                    for reservation in reservations:
                        print(reservation)
                else:
                    print("Aucune réservation a été faite")

                                
            elif choix == "15":
                disponibles = SalleCinemaDao.nombre_places_disponibles()
                if disponibles:
                    print(f"Nombre de places disponibles: {disponibles}")
                else:
                    print(disponibles)
                    

            elif choix == "16":
                nom = input("Nom de la personne qui a faite la réservations : ")
                reservations, message =SalleCinemaDao.filtrer_reservations_par_personne(nom)   
                if reservations:
                    for reservation in reservations:
                        print(reservation)
                else:
                    print(message)


            elif choix == "17":
                nom = input("Nom de la personne pour annuler les réservations : ")
                message = SalleCinemaDao.annuler_reservation(nom)
                print(message)
                
            elif choix == "18":
                print("Au revoir!")
                break
            else:
                  print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 et 7.")
               
saisie()           