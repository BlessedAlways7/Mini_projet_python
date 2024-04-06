#from listePersonnes.listePersonne import Personnes
#from listePersonnes.listePersonne_dao import ListePersonnesDao

from listePersonne import Personnes
from listePersonne_dao import ListePersonnesDao

def choix_option():
      print("\n\tMenu Principal : \n"
           "\t[1] Ajouter une personne à la liste.\n"
           "\t[2] Afficher les détails des personnes dans la liste.\n"
           "\t[3] Rechercher une personne dans la liste.\n"
           "\t[4] Filtrer personnes par son age.\n"
           "\t[5] Quitter le programme.\n")
     

def saisie():
        listepersonneDao = ListePersonnesDao
        while True:
               choix_option()
               choix = input("Veuillez choisir parmi les options suivantes: ")

               if choix =="1":
                    nom = input("Nom de la personne: ")
                    prenom = input("Prénom de la personne: ")
                    genre = input("Genre de la personne (masculin ou féminin): ")
                    age = input("Age de la personne: ")
                    personne = Personnes(nom,prenom,genre,age)
                    ListePersonnesDao.ajouter_personne(personne)
                    print(f"{nom} a été ajouté avec succes")

               elif choix == "2":
                    message, personnes =ListePersonnesDao.afficher_personnes()
                    if personnes:
                         print(message)
                         for personne in personnes:
                              print(personne)
                    else:
                              print(message)
                    
               elif choix == "3":
                    nom = input("Entrez le nom de la personne que vous cherchez : ")
                    personne  = ListePersonnesDao.rechercher_personne(nom)
                    if personne:
                         print(f"{nom} est dans notre  base de donnée")       
                    else:
                        print(f"{nom} n'est pas dans notre base de donnée.")
                             
               elif choix == "4":
                    min_age = int(input("Age minimum: "))
                    max_age = int(input("Age maximum: "))
                    personnes_filtrees = ListePersonnesDao.filtrer_personnes_par_age (min_age, max_age)
                    if personnes_filtrees:
                         for personne in personnes_filtrees:
                              print(personne)
                    else:
                          print ("Aucune personne ne correspond à votre tranche d'âge.")
                         
               elif choix == "5":
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 a 5.")

saisie()
      
                