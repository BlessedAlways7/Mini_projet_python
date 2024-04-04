
import database
from salle_Cinema.reservations import Reservations


class SalleCinemaDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, nom, place):
        if cls._places_disponibles() > 0 :
            sql = """INSERT INTO Reservations (nom, place)
                     VALUES (%s, %s)
                 """
            params = (nom,place)
            SalleCinemaDao.cursor.execute(sql,params)
            SalleCinemaDao.connexion.commit()
            print(f"{nom} a réservé la place {place}.")
        else:
            print("Désole, il n'y a plus de places disponibles.")


    @classmethod
    def afficher_places_reservees(cls):
        sql = """SELECT * FROM Reservations"""
        SalleCinemaDao.cursor.execute(sql)
        resultats = SalleCinemaDao.cursor.fetchall()
        for row in resultats:
            print(f"La personne {row[1]} à réservé la place {row[2]}.")


    @classmethod
    def places_disponibles(cls):
        return cls._places_totales() - cls._places_reservees()


    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = """SELECT *FROM Reservations WHERE nom = %s"""
        params = (nom,)
        SalleCinemaDao.cursor.execute(sql,params)
        resultat = SalleCinemaDao.cursor.fetchall()
        for row in resultat:
            print(f"La personne {nom} a réservé la place {row[2]}.")


    @classmethod
    def annuler_reservation(cls,nom):
        sql = """DELETE FROM Reservations WHERE nom = %s"""
        params = (nom,)
        SalleCinemaDao.cursor.execute(sql, params)
        SalleCinemaDao.connexion.commit()
        print(f"La reservation de {nom} a été annulée.")


    @classmethod
    def reserver_place_speciale(cls,nom):
        sql = """INSERT INTO Reservations (nom, place, speciale)
                     VALUES (%s, %s, 1)
                 """ 
        params = (nom, "spéciale")
        SalleCinemaDao.cursor.execute(sql,params)
        SalleCinemaDao.connexion.commit()
        print(f"{nom} a réserve la place spéciale.")

    @classmethod
    def places_totales(cls):
        return 200
    
    @classmethod
    def places_reservees(cls):
        sql = """SELECT COUNT(*) FROM Reservations WHERE speciale = 0"""
        SalleCinemaDao.cursor.execute(sql)
        resultat = SalleCinemaDao.cursor.fetchone()
        return resultat[0] if resultat else 0
    
    @classmethod
    def places_disponibles(cls):
        return cls.places_totales() - cls.places_reservees()
    

      