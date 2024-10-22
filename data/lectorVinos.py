import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modelos.Vino import Vino

db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
'SELECT * FROM VINOS')

vinos = cursor.fetchall()

listaVinos = []


for vino in vinos:
    idBodega = vino[6]
    idVarietal = vino[7]

    cursor.execute(
        'SELECT * FROM BODEGAS WHERE Id_bodega = ?', (int(idBodega),)
    )
    bodega = cursor.fetchone()
    cursor.execute(
        'SELECT * FROM VARIETALES WHERE Id_varietal = ?', (int(idVarietal),)
    )
    variatales = cursor.fetchall()
    vino = Vino(vino[1], vino[2], vino[3], vino[4], vino[5], variatales, bodega)
    listaVinos.append(vino)
conexion.close()


def leerVinos():
    return listaVinos
