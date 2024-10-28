import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.modelos.Reseña import Reseña

class LectorReseñas:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerReseñas(self):
        self.cursor.execute(
            'SELECT * FROM RESENIAS'
        )

        reseñas = self.cursor.fetchall()
        listaReseñas = []

        for reseña in reseñas:
            reseña = Reseña(reseña[1], reseña[2], reseña[3], reseña[4])
            listaReseñas.append(reseña)
        self.conexion.close()
        return listaReseñas

if __name__ == '__main__':
    lector = LectorReseñas()
    lector.leerReseñas()