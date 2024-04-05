#from fileAttentes.fileAttente import FileAttente
#from fileAttentes.fileAttente_dao import fileAttenteDao

from fileAttente import FileAttente
from fileAttente_dao import fileAttenteDao

def choix_option():
      print("\n\tMenu Principal : \n"
           "\t[1] Ajouter une personne de la file d'attente.\n"
           "\t[2] Supprimer une personne de la file d'attente.\n"
           "\t[3] Ajouter une personne prioritaire à la file d'attente.\n"
           "\t[4] Supprimer une personne prioritaire de la file d'attente.\n"
           "\t[5] Quitter le programme.")
      choix = input("Veuillez choisir parmi les options suivantes: ")
      return choix



def ajout_personne_attente():
     nom = input("Nom de la personne que vous souhaiter ajouter a la file d'attente: ")
     prenom = input("Prenom de la personne que vous souhaiter ajouter a la file d'attente: ")
     return FileAttente(nom,prenom)
     
def saisie():
        fileAttente= fileAttenteDao()  
        while True:
               choix = choix_option()
               if choix =="1":
                    personne = ajout_personne_attente()
                    fileAttenteDao.ajouter_personne_en_attente(personne)

                    print(f"{nom} a été ajouté à la file d'attente avec succès.")
                    

               elif choix == "2":
                    personne_annulee = fileAttenteDao.supprimer_de_la_file_dattente(nom)
                    if personne_annulee:
                         print(f"{personne_annulee} a bien été retirée de la file d'attente.")
                    else:
                         print("Il n'y a personne en attente pour être annulé.")
                         
               elif choix == "3":
                    nom = input("Nom de la personne prioritaire à ajouter à la file d'attente : ")
                    fileAttenteDao.ajouter_personne_prioritaire(nom)
                    print(f"{nom} a été ajouté à la file d'attente prioritaire.")
                         
               elif choix == "4":
                    nom = input("Nom de la personne prioritaire à retirer de la file d'attente : ")
                    personne_retiree = fileAttenteDao.supprimer_de_la_file_dattente(nom)
                    if personne_retiree:
                         print(f"{nom} a été retiré de la file d'attente prioritaire.")
                    else:
                         print(f"{nom} n'a pas été trouvé dans la file d'attente prioritaire.")

               elif choix == "5":
                    print("Au revoir!")
                    break
               else:
                    print("\nChoix incorrect.\nVeuillez saisir un nombre entre 1 a 5.")

saisie()
      