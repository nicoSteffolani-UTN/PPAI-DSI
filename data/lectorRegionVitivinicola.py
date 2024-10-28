import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.modelos.RegionVitivinicola import RegionVitivinicola


class LectorRegionVitivinicola:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerRegiones(self):

        self.cursor.execute(
            'SELECT * FROM REGIONES'
        )

        regiones = self.cursor.fetchall()

        listaRegiones = []

        for region in regiones:
            region = RegionVitivinicola(region[1], region[2])
            listaRegiones.append(region)
        self.conexion.close()
        return listaRegiones


