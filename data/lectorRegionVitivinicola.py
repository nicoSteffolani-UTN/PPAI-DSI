import sqlite3
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modelos.RegionVitivinicola import RegionVitivinicola


db_path = os.path.join(os.path.dirname(__file__), 'datos_prueba.db')
conexion = sqlite3.connect(db_path)

cursor = conexion.cursor()

cursor.execute(
    'SELECT * FROM REGIONES'
)

regiones = cursor.fetchall()

listaRegiones = []

for region in regiones:
    idRegion = region[0]

    cursor.execute(
        'SELECT * FROM BODEGAS WHERE REGION = ?', (int(idRegion),)
    )
    bodegas = cursor.fetchall()

    region = RegionVitivinicola(region[1], region[2], bodegas)
    listaRegiones.append(region)


conexion.close()
