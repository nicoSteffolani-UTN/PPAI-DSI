#TODO: completar la interfaz
import openpyxl

wb = openpyxl.load_workbook('Ranking.xlsx')

hoja = wb.active
hoja.titulo = 'Ranking'

hoja['A1'] = 'Nombre'
hoja['A2'] = 'Clasificación de Sommelier'
hoja['A3'] = 'Calificación General'
hoja['A4'] = 'Precio Sugerido'
hoja['A5'] = 'Bodega'
hoja['A6'] = 'Varietal'
hoja['A7'] = 'Región'
hoja['A8'] = 'País'

for fila, datos in enumerate(listaFiltrada, start=2):
    hoja[f'A{fila}'] = datos.nombre
    hoja[f'B{fila}'] = datos.clasificacionSommelier
    hoja[f'C{fila}'] = datos.calificacionGeneral
    hoja[f'D{fila}'] = datos.precioSugerido
    hoja[f'E{fila}'] = datos.bodega
    hoja[f'F{fila}'] = datos.varietal
    hoja[f'G{fila}'] = datos.region
    hoja[f'H{fila}'] = datos.pais