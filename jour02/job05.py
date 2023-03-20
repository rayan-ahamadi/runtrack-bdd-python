import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='laplateforme',
    user='root',
    password='root')

cursor = conn.cursor()
query = "SELECT superficie FROM etage;"
cursor.execute(query)
result = cursor.fetchall()

print(result)
total = 0

for surperficie in result: 
    total += surperficie[0]

print(f"La superficie de la Plateforme est de {total} m2")