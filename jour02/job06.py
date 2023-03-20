import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='laplateforme',
    user='root',
    password='root')

cursor = conn.cursor()
query = "SELECT capacite FROM salles;"
cursor.execute(query)
result = cursor.fetchall()
Total= 0 

for capacite in result : 
    Total += capacite[0]

print(f"La capacité de toutes les salles est de : {Total}")
