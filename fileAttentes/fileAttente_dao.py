import database
#from fileAttentes.fileAttente import FileAttente
import fileAttente

class FileAttenteDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_personne_en_attente(cls, nom,prenom):
        sql = """INSERT INTO FileAttente (nom, prenom, prioritaire) 
                 VALUES (%s, %s, 0)
              """
        params= (nom,prenom)
        try:
            FileAttenteDao.cursor.execute(sql,params)
            FileAttenteDao.connexion.commit()
            
            return f"{nom} est ajouté à la file d'attente avec succès"
        except Exception as error:
            return None, (f"Une erreur est survenue, veuillez recommencer: {error}")
          
    
    
    @classmethod
    def ajouter_personne_prioritaire(cls,nom,prenom):
        sql = """INSERT INTO FileAttente (nom,prenom, prioritaire) VALUES (%s,%s, 1)"""
        params = (nom,prenom)
        try:
            FileAttenteDao.cursor.execute(sql,params)
            FileAttenteDao.connexion.commit()
        
            return (f"{nom} a été ajouté à la file d'attente en tant que personne prioritaire avec succès.")
        except Exception as error:
            return (f"{nom} n'a pas été ajouté à la file d'attente en tant que personne prioritaire avec succès.")

    
    @classmethod
    def supprimer_de_la_file_dattente(cls, nom):
        sql_prio = """SELECT nom FROM FileAttente WHERE prioritaire = 1 AND nom= %s"""
        FileAttenteDao.cursor.execute(sql_prio, (nom,))
        personneEnPremier = FileAttenteDao.cursor.fetchone()
        
        if personneEnPremier is not None:
            sql = "DELETE FROM FileAttente WHERE nom = %s AND prioritaire = 1"
            FileAttenteDao.cursor.execute(sql,(nom,))
            FileAttenteDao.connexion.commit()
            return (f"{nom} a été retirée de la file d'attente prioritaire.")
        
        else :
            sql_normal = """SELECT nom FROM FileAttente WHERE prioritaire = 0 and nom= %s"""
            FileAttenteDao.cursor.execute(sql_normal, (nom,))
            personneNormal = FileAttenteDao.cursor.fetchone()

            if personneNormal is not None:
                sql = """DELETE FROM FileAttente WHERE nom = %s AND prioritaire = 0"""
                FileAttenteDao.cursor.execute(sql,(nom,))
                FileAttenteDao.connexion.commit()
                
                return (f"{nom} a été retirée de la file d'attente non prioritaire.")
            else :
                return (f"{nom} n'a pas été trouvée de la file d'attente.")
    


            
           

        
              