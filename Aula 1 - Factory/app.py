from MySQLDB
from connection_factory import ConnectionFactory

#Factory x Builder: no Factory passamos nada na criação do objeto, diferentemente do Builder
connection = ConnectionFactory().get_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM cursor")

for linha in cursor:
    print(linha)

connection.close()