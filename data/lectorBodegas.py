import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.modelos.Bodega import Bodega


class LectorBodegas:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerBodegas(self, listaRegiones):

        self.cursor.execute(
            'SELECT * FROM BODEGAS'
        )

        bodegas = self.cursor.fetchall()
        
        listaBodegas = []

        for bodega in bodegas:
            idRegion = bodega[5]
            self.cursor.execute(
                'SELECT * FROM REGIONES WHERE id_region_vitivinicola = ?', (int(idRegion),)
            )
            regiones = self.cursor.fetchone()
            
            for region in listaRegiones:
                if regiones[1] == region.getNombre():
                    regionVino = region
                

            bodega = Bodega(bodega[1], bodega[2], bodega[3], bodega[4], regionVino)
            listaBodegas.append(bodega)
        self.conexion.close()
        return listaBodegas


