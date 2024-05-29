import sqlite3
from modelos.Bodega import Bodega

conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM BODEGAS")

bodegas = cursor.fetchall()

listaBodegas = []

for bodega in bodegas:
    obj_bodega = Bodega(bodega[1], bodega[2], bodega[3], bodega[4], bodega[5])
    listaBodegas.append(obj_bodega)

conexion.close()

def leerBodegas():
    return listaBodegas