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
           "\t[5] Quitter le programme.")
      choix = input("Veuillez choisir parmi les options suivantes: ")
      return choix

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
                    ListePersonnesDao.ajouter_personne(personne)
                    print(f"La personne {nom} a été ajouté avec succes")

               elif choix == "2":
                    personne = ListePersonnesDao.afficher_personnes()
                    print(personne)
                    
               elif choix == "3":
                    nom = input("Entrez le nom de la personne que vous cherchez : ")
                    ListePersonnesDao.rechercher_personne(nom)
                    if nom:
                          print(ListePersonnesDao.rechercher_personne())
                          print(f"{nom} est dans la liste")       
                    else:
                        print("Cette personne n'est pas dans notre base de données.")
                             
               elif choix == "4":
                    min_age = int(input("Age minimum: "))
                    max_age = int(input("Age maximum: "))
                    personnes_filtrees = ListePersonnesDao.filtrer_personnes_par_age (min_age, max_age)
                    for personne in personnes_filtrees:
                         print(personne)
                         
               elif choix == "5":
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 a 5.")

saisie()
      
                