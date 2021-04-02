import MySQLDB

class ConnectionFactory:
    def get_connection(self):
        return MySQLDB.connect(
            host="localhost",
            user="root",
            passwd="",
            db="alura"
        )
