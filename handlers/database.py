import mysql.connector

class database_handler:
    def __init__(self, container, host, user, password, database):
        self.container = container
        db = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password
        )
        db_curser = db.cursor()
        db_curser.execute("CREATE DATABASE IF NOT EXISTS " + database + ";")

        self.db = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password,
            database = database
        )
        self.db_curser = self.db.cursor()
    

