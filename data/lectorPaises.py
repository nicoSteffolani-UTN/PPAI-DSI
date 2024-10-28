import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.modelos.Pais import Pais


class LectorPaises:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerPaises(self, listaProvincias):

        self.cursor.execute(
            'SELECT * FROM PAISES'
        )

        paises = self.cursor.fetchall()

        listaPaises = []

        for pais in paises:
            idPais = pais[0]
            provinciasPais = []

            self.cursor.execute(
                'SELECT NOMBRE FROM PROVINCIAS WHERE PAIS = ?', (int(idPais),)
            )
            provincias = self.cursor.fetchall()
            for provincia in provincias:
                for prov in listaProvincias:
                    if provincia[0] == prov.getNombre():
                        provinciasPais.append(prov)

            pais = Pais(pais[1], provinciasPais)
            listaPaises.append(pais)
        self.conexion.close()
        return listaPaises


