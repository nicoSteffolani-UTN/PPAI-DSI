import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.modelos.Varietal import Varietal

class LectorVarietal:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerReseñas(self):
        self.cursor.execute(
            'SELECT * FROM VARIETALES'
        )

        varietales = self.cursor.fetchall()
        listaVarietales = []

        for varietal in varietales:
            
            varietalVino = Varietal(varietal[1], varietal[2]) 
            listaVarietales.append(varietalVino)

        self.conexion.close()
        return listaVarietales

