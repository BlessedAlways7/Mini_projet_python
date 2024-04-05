from listePersonnes.listePersonne import Personnes
from listePersonnes.listePersonne_dao import ListePersonnesDao
from fileAttentes.fileAttente import FileAttente
from fileAttentes.fileAttente_dao import fileAttenteDao
from salle_Cinema.reservations import Reservations
from salle_Cinema.salleCinema_dao import SalleCinemaDao

"""
pers1 = Personnes("St-Denis", "Samuel", "masculin", "21")

#("Lambert", "Joe", "masculin", "38")

data_pers = ListePersonnesDao.ajouter_personne(pers1)
print(data_pers)

(personnes, message) = ListePersonnesDao.afficher_personnes()
print(message, personnes)
"""

def choix_option():
     print("\n\tMenu Principal : \n"
           "\t[1] Ajouter une personne à la liste.\n"
           "\t[2] Afficher les détails des personnes dans la liste.\n"
           "\t[3] Rechercher une personne dans la liste.\n"
           "\t[4] Filtrer personnes par son age.\n"
           "\t[5] Ajouter une personne à la file d'attente.\n"
           "\t[6] Supprimer une personne de la file d'attente.\n"
           "\t[7] Ajouter une personne prioritaire à la file d'attente.\n"
           "\t[8] Supprimer une personne prioritaire de la file d'attente.\n"
           "\t[9] Reserver une place pour une personne.\n"
           "\t[10] Afficher les places reservees.\n"
           "\t[11] Afficher les places disponibles.\n"
           "\t[12] Afficher les r/servations faites par une personne sp/cifique.\n"
           "\t[13] Annuler réservations faites par une personne spécifique.\n"
           "\t[14] Réserver une pplace spéciale pour une personne handicapée.\n"
           "\t[15] Quitter le programme.")
     while True:
        choix = input("\nVeuillez saisir votre choix (1 à 15): ")
        if choix.isdigit():
            choix = int(choix)
            if 1 <= choix <= 15:
                return choix
            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 15.")
        else:
            print("Choix invalide. Veuillez saisir un nombre entier.")
            
choix_option()
       
def ajout_personne():
     nom = input("Nom de la personne: ")
     prenom = input("Prénom de la personne: ")
     genre = input("Genre de la personne (masculin ou féminin): ")
     age = input("Age de la personne: ")
     return Personnes(nom,prenom,genre,age)

def saisie():
        personne= Personnes()  
        while True:
               choix = choix_option()
               if choix =="1":
                    personne = ajout_personne()        
                    ListePersonnesDao,ajout_personne(personne)
                    print(f"La personne {nom, prenom} a été ajouté avec succes")

               elif choix == "2":
                    print(Personnes)
                    
               elif choix == "3":
                    nom = input("Entrez le nom de la personne que vous cherchez : ")
                    resultat = ListePersonnesDao.rechercher_personne(nom)
                    if resultat is None:
                         print("Cette personne n'est pas dans notre base de données.")
                    else:
                         print(f"{resultat} est dans la liste")
                    
               elif choix == "4":
                    min_age = int(input("Age minimum: "))
                    max_age = int(input("Age maximum: "))
                    personnes_filtrees = ListePersonnesDao.filtrer_personnes_par_age (min_age, max_age)
                    for personne in personnes_filtrees:
                         print(personne)

               elif choix == "5":
                    nom = input("Nom de la personne que vous souhaiter a la file d'attente: ")
                    fileAttenteDao.ajouter_personne_en_attente(nom)
                    personne = fileAttenteDao(nom)
                    if personne:
                         print(f"{nom} a été ajouté à la file d'attente avec succès.")
                    else:
                         print(f"Une erreur est survenue lors de l'ajout de {nom} à la file d'attente.")   

               elif choix == "6":
                    personne_annulee = fileAttenteDao.supprimer_de_la_file_dattente(nom)
                    if personne_annulee:
                         print(f"{personne_annulee} a bien été retirée de la file d'attente.")
                    else:
                         print("Il n'y a personne en attente pour être annulé.")
                         
               elif choix == "7":
                    nom = input("Nom de la personne prioritaire à ajouter à la file d'attente : ")
                    fileAttenteDao.ajouter_personne_prioritaire(nom)
                    print(f"{nom} a été ajouté à la file d'attente prioritaire.")
                         
               elif choix == "8":
                    nom = input("Nom de la personne prioritaire à retirer de la file d'attente : ")
                    personne_retiree = fileAttenteDao.supprimer_de_la_file_dattente(nom)
                    if personne_retiree:
                         print(f"{nom} a été retiré de la file d'attente prioritaire.")
                    else:
                         print(f"{nom} n'a pas été trouvé dans la file d'attente prioritaire.")
               
               elif choix == "9":
                    nom = input("Nom de la personne à réserver une place pour : ")
                    place = input("Numéro de la place à réserver : ")
                    SalleCinemaDao.reserver_place(nom, place)

               elif choix == "10":
                    print("Les places réservées sont:")
                    SalleCinemaDao.afficher_places_reservees()

               elif choix == "11":
                    print(f"Il y a {SalleCinemaDao.places_disponibles()} places disponibles.")

               elif choix == "12":
                    nom = input("Nom de la personne pour afficher les réservations : ")
                    SalleCinemaDao.filtrer_reservations_par_personne(nom)   
                    
               elif choix == "13":
                    nom = input("Nom de la personne pour annuler les réservations : ")
                    SalleCinemaDao.annuler_reservation(nom)

               elif choix == "14":
                    nom = input("Nom de la personne à réserver une place spéciale pour : ")
                    SalleCinemaDao.reserver_place_speciale(nom)

               elif choix == "15":
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 et 15.")
               
saisie()           
      

          
   





