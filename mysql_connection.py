import mysql.connector

def dbConnection():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="library",
        )

