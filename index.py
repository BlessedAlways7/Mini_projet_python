
from listePersonnes.listePersonne import Personnes
from listePersonnes.listePersonne_dao import ListePersonnesDao
from fileAttentes.fileAttente import FileAttente
from fileAttentes.fileAttente_dao import FileAttenteDao
from salle_Cinema.reservations import Reservations
from salle_Cinema.salleCinema_dao import SalleCinemaDao

# Création du Menu Principale.     
def choix_option():
     print("\n\tMenu Principale : \n"
           "\t[1] Ajouter une personne à la liste.\n"
           "\t[2] Rechercher une personne dans la liste.\n"
           "\t[3] Filtrer les personnes par tranche d'âge.\n"
           "\t[4] Afficher les détails des personnes dans la liste.\n"
           "\t[5] Ajouter une personne à la file d'attente.\n"
           "\t[6] Ajouter une personne prioritaire à la file d'attente.\n"
           "\t[7] Supprimer une personne de la file d'attente.\n"
           "\t[8] Réserver une place.\n"
           "\t[9] Réserver une place spéciale pour une personne en besoin d'assistance.\n"
           "\t[10] Filtrer les réservations faites par une personne.\n"
           "\t[11] Afficher les réservations.\n"
           "\t[12] Afficher les places disponibles.\n"
           "\t[13] Annuler réservations faites par une personne.\n"
           "\t[14] Quitter le programme. \n")
                 
def saisie(): 
         while True:
               choix = choix_option()
               choix = input("\nVeuillez saisir votre choix entre 1 à 14: ")

               if choix =="1":
                    nom = input("Nom de la personne: ")
                    prenom = input("Prénom de la personne: ")
                    genre = input("Genre de la personne, masculin ou féminin: ")
                    age = input("Âge de la personne: ")
                    personne = Personnes(nom,prenom,genre,age)
                    ListePersonnesDao.ajouter_personne(personne)
                    print(f"{nom} {prenom} a été ajouté(e) avec succes")

               elif choix == "2":
                    nom = input("Entrez le nom de la personne que vous cherchez: ")
                    personne  = ListePersonnesDao.rechercher_personne(nom)
                    if personne:
                         print(f"{nom} est dans la base de donnée.")       
                    else:
                        print(f"{nom} n'est pas dans la base de donnée.")   
                          
               elif choix == "3":
                    min_age = int(input("Âge minimum: "))
                    max_age = int(input("Âge maximum: "))
                    personnes_filtrees = ListePersonnesDao.filtrer_personnes_par_age (min_age, max_age)
                    if min_age >=1:
                         personnes_filtrees = ListePersonnesDao.filtrer_personnes_par_age (min_age, max_age)
                         if personnes_filtrees:
                              for personne in personnes_filtrees:
                                   print(personne)
                         else:
                              print ("Aucune personne ne correspond à votre tranche d'âge.")
                    else:
                          print("Veuillez saisir des nombres supérieur ou égale a 1.")

               elif choix == "4":
                    message, personnes =ListePersonnesDao.afficher_personnes()
                    if personnes:
                         print(message)
                         for personne in personnes:
                              print(personne)
                    else:
                              print(message)

               elif choix =="5":
                    nom = input("Nom de la personne que vous souhaiter ajouter a la file d'attente: ")
                    prenom = input("Prénom de la personne que vous souhaiter ajouter a la file d'attente: ")
                    FileAttenteDao.ajouter_personne_en_attente(nom, prenom)
                    print(f"{nom} {prenom} a été ajouté(e) à la file d'attente avec succès.")
               
               elif choix == "6":
                    nom = input("Nom de la personne prioritaire à ajouter à la file d'attente : ")
                    prenom = input("Prénom de la personne prioritaire que vous souhaiter ajouter a la file d'attente: ")
                    FileAttenteDao.ajouter_personne_prioritaire(nom,prenom)
                    print(f"{nom} {prenom} a été ajouté(e) à la file d'attente prioritaire.")

               elif choix == "7":
                    nom= input("Nom de la personne que vous souhaiter supprimer de la file d'attente: ")
                    message=FileAttenteDao.supprimer_de_la_file_dattente(nom)
                    print(message)

               elif choix =="8":
                    nom = input("Nom de la personne qui veut réservée une place: ")
                    prenom = input("Prénom de la personne qui veut réservée une place: ")
                    place = input("Nombre de place réservé : ") 
                    SalleCinemaDao.reserver_place(nom, prenom, place) 
                    print(f"{nom} {prenom} a été ajouté à la réservation avec succès.")

               elif choix == "9":
                    nom = input("Nom de la personne pour laquelle il faut réserver une place spéciale: ")
                    prenom = input("Prénom de la personne pour laquelle il faut réserver une place spéciale: ")
                    place_speciale = input("Nombre de place spéciale a réservé: ")
                    print(SalleCinemaDao.reserver_place_speciale(nom,prenom, place_speciale))   

               elif choix == "10":
                    nom = input("Nom de la personne qui a fait la réservations: ")
                    reservations, message =SalleCinemaDao.filtrer_reservations_par_personne(nom)   
                    print(message)

               elif choix == "11":
                    message, reservations = SalleCinemaDao.afficher_places_reservees()
                    if reservations:
                         print(message)
                         for reservation in reservations:
                              print(reservation)
                    else:
                         print("Aucune réservation a été faite.")
             
               elif choix == "12":
                    disponibles = SalleCinemaDao.nombre_places_disponibles()
                    if disponibles > 0:
                         print(f"Il y a encore {disponibles} places disponibles dans le cinéma.")
                    else:
                         print("Aucune place disponible, veuillez ressayer plus tard!")
                    
               elif choix == "13":
                    nom = input("Nom de la personne pour annuler les réservations : ")
                    message = SalleCinemaDao.annuler_reservation(nom)
                    print(message)

               elif choix == "14":
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 et 14.")

saisie()           
      