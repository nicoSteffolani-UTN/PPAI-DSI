import sqlite3
import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
from backend.modelos.Provincia import Provincia

class LectorProvincias:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerProvincias(self, listaRegiones):

        self.cursor.execute(
            'SELECT * FROM PROVINCIAS'
        )

        provincias = self.cursor.fetchall()

        listaProvincias = []

        for provincia in provincias:
            idProvincia = provincia[0]
            regionesProvincia = []

            self.cursor.execute(
                'SELECT * FROM REGIONES WHERE PROVINCIA = ?', (int(idProvincia),)
            )
            regiones = self.cursor.fetchall()
            for region in regiones:
                for reg in listaRegiones:
                    if region[1] == reg.getNombre():
                        regionesProvincia.append(reg)

            provincia = Provincia(provincia[1], regionesProvincia)
            listaProvincias.append(provincia)
        self.conexion.close()
        return listaProvincias
