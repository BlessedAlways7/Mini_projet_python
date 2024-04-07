
import database
from salle_Cinema.reservations import Reservations

# Création de la classe SalleCinemaDao
class SalleCinemaDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

# Méthode reserver_place pour réserver une place dans la Salle Cinéma.

    @classmethod
    def reserver_place(cls, nom, prenom, place):
        sql = "INSERT INTO reservations (nom, prenom, place, place_speciale) VALUES (%s,%s, %s, 0)"
        params = (nom, prenom, place)   
        try:
            SalleCinemaDao.cursor.execute(sql, params)
            SalleCinemaDao.connexion.commit()    
            print(f"{nom} {prenom} a réservé {place} place.")          
        except Exception as error:
            return f"Erreur lors de la reservation: {error}"

# Méthode reserver_place_speciale pour réserver une place spéciale dans la Salle Cinéma.   
  
    @classmethod
    def reserver_place_speciale(cls,nom, prenom, place_speciale):
        sql = """INSERT INTO reservations (nom, prenom, place, place_speciale) VALUES (%s, %s, 0, %s)""" 
        params = (nom, prenom, place_speciale)
        try:   
            SalleCinemaDao.cursor.execute(sql,params)
            SalleCinemaDao.connexion.commit()
            return (f"{nom} a réserve {place_speciale} place spéciale.") 
        except Exception as error:
            return f"Impossible d'effectuer cette opération: {error}"

# Méthode afficher_places_reservees pour afficher les places dans la Salle Cinéma.     

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

# Méthode places_reservees pour calculer le nombres de réservations de la Salle Cinéma. 
            
    @classmethod
    def places_reservees(cls):
        sql = "SELECT SUM(place) FROM reservations"
        try:
            SalleCinemaDao.cursor.execute(sql)
            nombre_reservations = SalleCinemaDao.cursor.fetchone()[0]
            print (f"Nombre de reservations: {nombre_reservations}")
            return nombre_reservations   
        except Exception as error:
            print (f"Erreur lors de la récupération des réservations! {error}")
            return 0

# Méthode nombre_places_disponibles pour calculer les places disponibles dans la Salle Cinéma.    
 
    @classmethod
    def nombre_places_disponibles(cls):
        capacite_totale= 200
        try:
            reservations= SalleCinemaDao.places_reservees()
            disponibles = capacite_totale - reservations
            return disponibles if disponibles >= 0 else 0          
        except Exception as error:
            print(f"Erreur lors du calcul des places disponibles!", error)
            return 0

# Méthode filtrer_reservations_par_personnes pour afficher la réservation Salle Cinéma d'une personne.   
  
    @classmethod
    def filtrer_reservations_par_personne(cls,nom):
        sql = """SELECT *FROM reservations WHERE nom = %s"""
        try:
            SalleCinemaDao.cursor.execute(sql,(nom,))
            reservations = SalleCinemaDao.cursor.fetchall()
            if reservations:
                message = f"{nom} a réservé une place."          
            else:
                return None, f" Malheureusement, aucune reservation à été fait pour {nom}!"
            return reservations,message
        except Exception as error:
           return None, f"Erreur lors de la récupération des réservations : {error}"
        
# Méthode annuler_reservation pour annuler une réservation dans la Salle Cinéma.  
   
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
        
    