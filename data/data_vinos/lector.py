import sqlite3

conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PAISES")

paises = cursor.fetchall()

for pais in paises:
    print(pais)

conexion.close()

sqlite3 datos_prueba.db ".recover" | sqlite3 datos_prueba_reparada.db