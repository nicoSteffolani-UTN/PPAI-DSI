import sqlite3
from modelos.Pais import Pais


conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PAISES")

paises = cursor.fetchall()

listaPaises = []

for pais in paises:
    obj_pais = Pais(pais[1])
    listaPaises.append(obj_pais)

conexion.close()

def leerPaises():
    return listaPaises
