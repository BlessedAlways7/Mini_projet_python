
import database
#from salle_Cinema.reservations import Reservations
import reservations


class SalleCinemaDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def reserver_place(cls, nom, prenom, place):
        sql = """INSERT INTO reservations (nom, prenom, place, place_speciale)
                        VALUES (%s,%s, %s, 0)
                      """
        params = (nom, prenom, place)
        
        try:
            SalleCinemaDao.cursor.execute(sql, params)
            SalleCinemaDao.connexion.commit()

            if SalleCinemaDao.nombre_places_disponibles() > 0 :
                
                return (f"{nom} {prenom} a réservé {place} place.")
            else:
                print("Désole, il n'y a plus de places disponibles.")
        except Exception as error:
            return f"Erreur lors de la reservation: {error}"
        
    @classmethod
    def reserver_place_speciale(cls,nom, prenom, place_speciale):
        sql = """INSERT INTO reservations (nom, prenom, place, place_speciale)
                     VALUES (%s, %s, 0, %s)
                 """ 
        params = (nom, prenom, place_speciale)
        try:   
            SalleCinemaDao.cursor.execute(sql,params)
            SalleCinemaDao.connexion.commit()
            return (f"{nom} a réserve {place_speciale} place spéciale.")
        except Exception as error:
            return f"Impossible d'effectuer cette opération: {error}"


    @classmethod
    def afficher_places_reservees(cls):
        sql = """SELECT * FROM reservations"""
        try:
            SalleCinemaDao.cursor.execute(sql)
            reservations = SalleCinemaDao.cursor.fetchall()
            message = "Voici les réservations!", reservations
        except Exception as error:
            message= f"Erreur lors de l'affichage des réservations : {error}"
        return message
        
        
    @classmethod
    def places_reservees(cls):
        sql = """SELECT COUNT(*) FROM reservations"""
        try:
            SalleCinemaDao.cursor.execute(sql)
            reservations = SalleCinemaDao.cursor.fetchone()[0]
            print(f"Reservation total: {reservations}")
            return reservations
        except Exception as error:
            return f"Erreur lors de la récupération des réservations!"
        

    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale= 200
        sql = "SELECT COUNT(*) FROM reservations WHERE place_speciale = 0"
        try:
            SalleCinemaDao.cursor.execute(sql)
            reservations= SalleCinemaDao.cursor.fetchone()[0]
           
            disponibles = capacite_totale - reservations
            print(f" Reservation total: {reservations}")
            print(f"Capacite total: {capacite_totale}")
            print(f" place disponibles: {disponibles}")
            return disponibles if disponibles > 0 else 0 
            
        except Exception as error:
            return(f"Erreur lors du calcul des places disponibles!")
        

    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = """SELECT *FROM reservations WHERE nom = %s"""
        try:
            SalleCinemaDao.cursor.execute(sql,(nom,))
            reservations = SalleCinemaDao.cursor.fetchall()
            if reservations:
                return reservations, f"La personne {nom} a réservé la place."
            else:
                return None, f" Malheureusement, aucune reservation à été fait pour {nom}!"
        except Exception as error:
           return None, f"Erreur lors de la récupération des réservations : {error}"
        

    @classmethod
    def annuler_reservation(cls,nom):
        sql = """DELETE FROM reservations WHERE nom = %s"""
        try:
            SalleCinemaDao.cursor.execute(sql, (nom,))
            SalleCinemaDao.connexion.commit()
            if SalleCinemaDao.cursor.rowcount > 0:
                return f"La réservation au nom {nom} a bien été annulée."
            else:
                return f"Impossible d'annuler cette réservation car elle n'existe pas."
        except Exception as error:
            return f"Une erreur est survenue lors de l'annulation de la réservation : {error}"
           
               
 
        
    

      