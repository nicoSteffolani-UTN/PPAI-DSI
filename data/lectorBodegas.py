import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from modelos.Bodega import Bodega



db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
    'SELECT * FROM BODEGAS'
)

bodegas = cursor.fetchall()

listaBodegas = []

for bodega in bodegas:
    idBodega = bodega[0]

    cursor.execute(
        'SELECT * FROM VINOS WHERE BODEGA = ?', (int(idBodega),)
    )
    vinos = cursor.fetchall()

    bodega = Bodega(bodega[1],bodega[2],bodega[3],bodega[4], vinos)
    listaBodegas.append(bodega)



conexion.close()

