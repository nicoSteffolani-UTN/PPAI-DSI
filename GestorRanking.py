from data.dataVinos.lectorReseña import leerReseñas
from data.dataVinos.lectorVinos import leerVinos


class GestorRanking():
    
    def __init__(self, fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoRes = tipoReseña
        self.tipoVis = tipoVisualizacion
        
        
    
    def buscarReseñasEnPeriodo(self, idVino):
        listaReseñas = leerReseñas()
        
        listaFiltrada = []

        for reseña in listaReseñas:
            if (reseña.validarFechaPeriodo(self.fechaDesde, self.fechaHasta) and reseña.sosDeVino(idVino)):
                
                if self.tipoRes == 'sommelier'and reseña.esPremium:
                        return True

                elif self.tipoRes == 'normal':
                    return True

                elif self.tipoRes == 'amigos':
                    if not(reseña.esPremium):
                        return True
                    
        return False


    def buscarVinosReseñasEnPeriodo(self):
        listaVinos = leerVinos()
        listaFiltrada = []

        for vino in listaVinos:

            if GestorRanking.buscarReseñasEnPeriodo(self, vino.id):
                listaFiltrada.append(vino)
        
        return listaFiltrada

    def calcularPuntajePromedio(cant, sum):
        prom = sum/cant
        return round(prom, 2)

    def calcularPuntajeDeSommelierEnPeriodo(self, lista):
        listaRanking = []
        listaReseñas = leerReseñas()

        for vino in lista:
            puntaje = 0
            cantidad = 0
            puntajeGen = 0
            cantGen = 0

            for reseña in listaReseñas:
                if reseña.sosDeVino(vino.id) and reseña.esPremium and reseña.validarFechaPeriodo(self.fechaDesde, self.fechaHasta):                   
                    puntaje += reseña.puntaje
                    cantidad += 1

                if reseña.sosDeVino(vino.id) and reseña.validarFechaPeriodo(self.fechaDesde, self.fechaHasta):
                    puntajeGen += reseña.puntaje
                    cantGen += 1
                    print(puntajeGen, cantGen)

                
            
            prom = GestorRanking.calcularPuntajePromedio(cantidad, puntaje)
            promGen = GestorRanking.calcularPuntajePromedio(cantGen, puntajeGen)

            lista = [vino.getDatosVino(), prom, promGen]
            listaRanking.append(lista)
        return listaRanking
    
    def ordenarVinos(self, listaRanking):
        
        listaOrdenada = sorted(listaRanking, key=lambda x: x[1], reverse=True)
        return listaOrdenada[:10]
    

