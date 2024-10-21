import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modelos.Reseña import Reseña


db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
    'SELECT * FROM RESENIAS'
)

reseñas = cursor.fetchall()
print(reseñas);
listaReseñas = []

for reseña in reseñas:
    idVino = reseña[5]
    cursor.execute(
        'SELECT * FROM VINOS WHERE id_vino = ?', (int(idVino),)
    )
    vino = cursor.fetchone()
    reseña = Reseña(reseña[0], reseña[1], reseña[2], reseña[3], reseña[4], vino)
    listaReseñas.append(reseña)
conexion.close()


def leerReseñas():
    return listaReseñas
