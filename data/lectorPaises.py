import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modelos.Pais import Pais


db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
    'SELECT * FROM PAISES'
)

paises = cursor.fetchall()

listaPaises = []

for pais in paises:
    idPais = pais[0]
    nomProvincias = []

    cursor.execute(
        'SELECT NOMBRE FROM PROVINCIAS WHERE PAIS = ?', (int(idPais),)
    )
    provincias = cursor.fetchall()
    for provincia in provincias:
        nomProvincias.append(provincia[0])
    print(nomProvincias)

    pais = Pais(pais[1], nomProvincias)
    listaPaises.append(pais)


conexion.close()

