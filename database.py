import mysql.connector as mysql

#Initiation de la connextion a la base de données.

def connect_db():
    return mysql.connect(
    user = "root", 
    password = "",
    host = "localhost",
    database = "gestion"
)
