import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.modelos.Vino import Vino

class LectorVinos:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def leerVinos(self, listaBodegas, listaVarietales, listaReseñas):

        self.cursor.execute(
            'SELECT * FROM VINOS')

        vinos = self.cursor.fetchall()

        listaVinos = []

        for vino in vinos:
            idBodega = vino[6]
            idVarietal = vino[7]
            idVino = vino[0]
            reseñasVino = []

            self.cursor.execute(
                'SELECT * FROM BODEGAS WHERE Id_bodega = ?', (int(idBodega),)
            )
            bodega = self.cursor.fetchone()
            nomBodega = bodega[1]

            for bodega in listaBodegas:
                if bodega.getNombre() == nomBodega:
                    bodegaVino = bodega

            self.cursor.execute(
                'SELECT * FROM VARIETALES WHERE Id_varietal = ?', (int(idVarietal),)
            )
            variatales = self.cursor.fetchone()
            nomVarietal = variatales[1]

            for varietal in listaVarietales:
                if varietal.getDescripcion() == nomVarietal:
                    varietalVino = varietal
            
            self.cursor.execute(
                'SELECT * FROM RESENIAS WHERE vino = ?', (int(idVino),)
            )
            reseñas = self.cursor.fetchall()

            for reseña in reseñas:
                for res in listaReseñas:
                    if reseña[1] == res.getComentario() and reseña[2] == res.getPuntaje() and reseña[3] == res.getFechaReseña():
                        reseñasVino.append(reseña)

            vino = Vino(vino[1], vino[2], vino[3], vino[4], vino[5], varietalVino, bodegaVino, reseñasVino)
            listaVinos.append(vino)
        self.conexion.close()
        return listaVinos



