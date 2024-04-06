#from fileAttentes.fileAttente import FileAttente
#from fileAttentes.fileAttente_dao import fileAttenteDao

from fileAttente import FileAttente
from fileAttente_dao import FileAttenteDao

def choix_option():
      print("\n\tMenu Principal : \n"
           "\t[7] Ajouter une personne de la file d'attente.\n"
           "\t[8] Ajouter une personne prioritaire à la file d'attente.\n"
           "\t[9] Supprimer une personne de la file d'attente.\n"
           "\t[10] Quitter le programme.\n")
      
     

     
def saisie():
        fileAttenteDao = FileAttenteDao
        while True:
               choix = choix_option()
               choix = input("Veuillez choisir parmi les options suivantes: ")

               if choix =="7":
                    nom = input("Nom de la personne que vous souhaiter ajouter a la file d'attente: ")
                    prenom = input("Prénom de la personne que vous souhaiter ajouter a la file d'attente: ")
                    FileAttenteDao.ajouter_personne_en_attente(nom, prenom)
                    print(f"{nom} a été ajouté à la file d'attente avec succès.")
               

               elif choix == "8":
                    nom = input("Nom de la personne prioritaire à ajouter à la file d'attente : ")
                    prenom = input("Prénom de la personne prioritaire que vous souhaiter ajouter a la file d'attente: ")
                    FileAttenteDao.ajouter_personne_prioritaire(nom,prenom)
                    print(f"{nom} a été ajouté à la file d'attente prioritaire.")


               elif choix == "9":
                    nom= input("Nom de la personne que vous souhaiter supprimer de la file d'attente: ")
                    message=FileAttenteDao.supprimer_de_la_file_dattente(nom)
                    print(message)


               elif choix == "10":
               
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 7 a 10.")

saisie()
      