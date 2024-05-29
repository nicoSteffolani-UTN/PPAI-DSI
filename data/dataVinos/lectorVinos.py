import sqlite3
from modelos.Vino import Vino
from modelos.Bodega import Bodega
from modelos.Varietal import Varietal
from modelos.RegionVitivinicola import RegionVitivinicola
from modelos.Provincia import Provincia
from modelos.Pais import Pais


conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute(
'SELECT V.id_vino, V.aniada, V.fecha_actualizacion, V.imagen_etiqueta, V.nombre, V.precio,\
		B.nombre, B.descripcion, B.historia, B.coordenadas,\
		R.descripcion, R.nombre,\
		P.nombre,\
		PA.nombre,\
		VA.descripcion, VA.porcent_comp\
    FROM VINOS V JOIN BODEGAS B ON V.BODEGA = B.ID_BODEGA \
                    JOIN VARIETALES VA ON V.VARIETAL = VA.ID_VARIETAL\
                    JOIN REGIONES R ON B.REGION = R.id_region_vitivinicola\
                    JOIN PROVINCIAS P ON R.PROVINCIA = P.ID_PROVINCIA\
                    JOIN PAISES PA ON P.PAIS = PA.ID_PAIS;')

vinos = cursor.fetchall()

listaVinos = []

for vino in vinos:
    obj_vino = Vino(
        vino[0], vino[1], vino[2], vino[3], vino[4], vino[5], 
        Bodega(vino[6], vino[7], vino[8], vino[9], 
               RegionVitivinicola(vino[10], vino[11], 
                    Provincia(vino[12], Pais(vino[13])))), 
        Varietal(vino[14], vino[15])
        )
    listaVinos.append(obj_vino)
    print(obj_vino)

conexion.close()


def leerVinos():
    return listaVinos
