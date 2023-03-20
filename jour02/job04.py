import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='laplateforme',
    user='root',
    password='root')

cursor = conn.cursor()
query = "SELECT nom,capacite FROM salles;"
cursor.execute(query)
print(cursor.fetchall())
