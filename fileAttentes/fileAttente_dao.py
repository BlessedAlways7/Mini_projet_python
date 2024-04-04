import database
from fileAttentes.fileAttente import FileAttente

class fileAttenteDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_personne_en_attente(cls, nom):
        sql = """INSERT INTO FileAttente (nom, prioritaire) 
                 VALUES (%s, 0)
              """
        params= (nom,)
        try:
            fileAttenteDao.cursor.execute(sql, params)
            fileAttenteDao.connexion.commit()
            fileAttenteDao.cursor.close()
            message = f"{nom} est ajouté à la file d'attente avec succès"
        except Exception as error:
            message  = (f"Une erreur est survenue, veuillez contacter l'administrateur")
            print (error)
        return message
    
    
    @classmethod
    def ajouter_personne_prioritaire(cls,nom):
        sql = """INSERT INTO FileAttente (nom, prioritaire) VALUES (%s, 1)"""
        params = (nom,)
        fileAttenteDao.cursor.execute(sql,params)
        fileAttenteDao.connexion.commit()
        fileAttenteDao.cursor.close()
        message = (f"{nom} a été ajouté à la file d'attente en tant que personne prioritaire avec succès.")
        return message

    
    @classmethod
    def supprimer_de_la_file_dattente(cls, nom):
        sql = """SELECT nom FROM FileAttente WHERE prioritaire = 1 ORDER BY id LIMIT 1"""
        fileAttenteDao.cursor.execute(sql)
        personneEnPremier = fileAttenteDao.cursor.fetchone()
        if personneEnPremier is not None and personneEnPremier[0] == nom :
            sql = "DELETE FROM FileAttente WHERE nom = %s"
            params=(nom, )
            fileAttenteDao.cursor.execute(sql,params)
            fileAttenteDao.connexion.commit()
            fileAttenteDao.cursor.close()
            message = (f"{nom} a été retirée de la file d'attente prioritaire.")
        else :
            sql_normal = """SELECT nom FROM FileAttente WHERE prioritaire = 0 ORDER BY id LIMIT 1"""
            fileAttenteDao.cursor.execute(sql_normal)
            personneNormal = fileAttenteDao.cursor.fetchone()
            if personneNormal:
                nom = personneNormal[0]
                sql = """DELETE FROM FileAttente WHERE nom = %s"""
                params = (nom,)
                fileAttenteDao.cursor.execute(sql, params)
                fileAttenteDao.connexion.commit()
                fileAttenteDao.cursor.close()
                message = (f"{nom} a été retirée de la file d'attente non prioritaire.")
            else :
                message = "La file d'attente est vide."
            return message


            
           

        
              