import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='laplateforme',
    user='root',
    password='root')

cursor = conn.cursor()

query = "SELECT * FROM etudiants;"
cursor.execute(query)
rows = cursor.fetchall()
print(rows)
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

conn.close()