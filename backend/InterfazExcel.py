import openpyxl

class InterfazExcel:
    @staticmethod
    def exportarExcel(listaOrdenada):
        wb = openpyxl.Workbook()

        hoja = wb.active
        hoja.title = 'Ranking'

        hoja['A1'] = 'Nombre'
        hoja['B1'] = 'Clasificación de Sommelier'
        hoja['C1'] = 'Calificación General'
        hoja['D1'] = 'Precio Sugerido'
        hoja['E1'] = 'Bodega'
        hoja['F1'] = 'Varietal'
        hoja['G1'] = 'Región'
        hoja['H1'] = 'País'

        for fila, datos in enumerate(listaOrdenada, start=2):
            hoja[f'A{fila}'] = datos[0]
            hoja[f'B{fila}'] = datos[1]
            hoja[f'C{fila}'] = datos[2]
            hoja[f'D{fila}'] = datos[3]
            hoja[f'E{fila}'] = datos[4]
            hoja[f'F{fila}'] = datos[5]
            hoja[f'G{fila}'] = datos[6]
            hoja[f'H{fila}'] = datos[7]

        wb.save('Ranking.xlsx')
