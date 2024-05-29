import sqlite3
from modelos.Vino import Vino


conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM VINOS")

vinos = cursor.fetchall()

listaVinos = []

for vino in vinos:
    obj_vino = Vino(vino[1])
    listaVinos.append(obj_vino)

conexion.close()

def leerVinos():
    return listaVinos
