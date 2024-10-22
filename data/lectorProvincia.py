import sqlite3
import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
from backend.modelos.Provincia import Provincia


db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
    'SELECT * FROM PROVINCIAS'
)

provincias = cursor.fetchall()

listaProvincias = []

for provincia in provincias:
    idProvincia = provincia[0]

    cursor.execute(
        'SELECT * FROM REGIONES WHERE PROVINCIA = ?', (int(idProvincia),)
    )
    regiones = cursor.fetchall()

    provincia = Provincia(provincia[1], regiones)
    listaProvincias.append(provincia)


conexion.close()
