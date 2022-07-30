import MySQLdb
db_host = "localhost"
db_schema = "library"
db_username = "root"
db_password = "password"
def dbConnection():

    mydb = MySQLdb.connect(
            host=db_host,
            user=db_username,
            passwd=db_password,
            database=db_schema,
            )
    return mydb