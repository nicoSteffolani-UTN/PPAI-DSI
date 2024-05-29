import sqlite3
from modelos.Vino import Vino
from modelos.Bodega import Bodega
from modelos.Varietal import Varietal
from modelos.RegionVitivinicola import RegionVitivinicola
from modelos.Provincia import Provincia
from modelos.Pais import Pais
from modelos.Reseña import Reseña


conexion = sqlite3.connect("datos_prueba.db")

cursor = conexion.cursor()

cursor.execute(
    'SELECT V.id_vino, V.aniada, V.fecha_actualizacion, V.imagen_etiqueta, V.nombre, V.precio,\
        B.nombre, B.descripcion, B.historia, B.coordenadas,\
        R.descripcion, R.nombre,\
        P.nombre,\
        PA.nombre,\
        VA.descripcion, VA.porcent_comp,\
        RE.ID_RESENIA, RE.COMENTARIO, RE.PUNTAJE, RE.FECHA_RESENIA, RE.ES_PREMIUM\
    FROM RESENIAS RE JOIN VINOS V ON RE.VINO = V.ID_VINO\
                    JOIN BODEGAS B ON V.BODEGA = B.ID_BODEGA \
                    JOIN VARIETALES VA ON V.VARIETAL = VA.ID_VARIETAL\
                    JOIN REGIONES R ON B.REGION = R.id_region_vitivinicola\
                    JOIN PROVINCIAS P ON R.PROVINCIA = P.ID_PROVINCIA\
                    JOIN PAISES PA ON P.PAIS = PA.ID_PAIS'
)

reseñas = cursor.fetchall()

listaReseñas = []

for reseña in reseñas:
    obj_reseña = Reseña(
        Vino( reseña[0], reseña[1], reseña[2], reseña[3], reseña[4], reseña[5], 
            Bodega(reseña[6], reseña[7], reseña[8], reseña[9], 
               RegionVitivinicola(reseña[10], reseña[11], 
                    Provincia(reseña[12], 
                        Pais(reseña[13])
                    )
                )
            ), 
            Varietal(reseña[14], reseña[15])
        ), reseña[16], reseña[17], reseña[18], reseña[19], reseña[20])
    listaReseñas.append(obj_reseña)

conexion.close()


def leerReseñas():
    return listaReseñas
