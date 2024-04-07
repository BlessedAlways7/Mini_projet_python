import database
from listePersonne import Personnes

        
class ListePersonnesDao:

    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

# Ajoutez une méthode ajouter_personne(nom, age) pour ajouter une nouvelle personne à la liste.

    @classmethod    
    def ajouter_personne(cls,pers:Personnes):
        sql = """INSERT INTO personnes (nom, prenom, genre,age) 
                 VALUES (%s, %s, %s, %s)
              """
        params= pers.nom, pers.prenom, pers.genre, pers.age
        try:
            
            ListePersonnesDao.cursor.execute(sql, params)
            ListePersonnesDao.connexion.commit()
            
            message = f"{pers.nom, pers.prenom} est ajouté avec succès"
        except Exception as error:
            message  = f"Une erreur est survenue, veuillez contacter l'administrateur"
            
        return message
       

    @classmethod
    def afficher_personnes(cls):
        sql = "SELECT * FROM personnes"
        try:
            ListePersonnesDao.cursor.execute(sql)
            personnes = ListePersonnesDao.cursor.fetchall()
            message = "Affichage réussi!"
           
        except Exception as error:
            message ="Une erreur empêche l'affichage"
            personnes = []
        return message, personnes
    

    @classmethod
    def rechercher_personne(cls, nom):
        sql ="SELECT * FROM personnes WHERE nom = %s"
        ListePersonnesDao.cursor.execute(sql,(nom,))
        personnes = ListePersonnesDao.cursor.fetchone()
        
        return personnes
    
    @classmethod
    def filtrer_personnes_par_age(cls, min_age, max_age):
        sql = "SELECT * FROM personnes WHERE age BETWEEN %s AND %s"
        ListePersonnesDao.cursor.execute(sql,(min_age, max_age))
        personnes = ListePersonnesDao.cursor.fetchall()
        
        return personnes
   