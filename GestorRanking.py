from data.lectorReseña import leerReseñas
from data.lectorVinos import leerVinos


class GestorAdmReporteRanking():
    
    def __init__(self, fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion):
        self.fechaDesde = fechaDesde
        self.fechaHasta = fechaHasta
        self.tipoRes = tipoReseña
        self.tipoVis = tipoVisualizacion
        
        
    def tomarFechasReseñas(req):
        fechaDesde = req.get('fechaDesde')
        fechaHasta = req.get('fechaHasta')
        return fechaDesde, fechaHasta
    
    def tomarTipoReseña(req):
        tipoReseña = req.get('tipoReseña')
        return tipoReseña
    
    def tomarTipoVisualizacion(req):
        tipoVisualizacion = req.get('tipoVisualizacion')
        return tipoVisualizacion

    def buscarReseñasEnPeriodo(self, idVino): #TODO: Volar este metodo a la mierda
        listaReseñas = leerReseñas()

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


    def buscarVinosReseñasEnPeriodo(self): #TODO: CORREGIRLO
        listaVinos = leerVinos()
        listaFiltrada = []

        for vino in listaVinos:

            idVino = vino.getId()

            if GestorAdmReporteRanking.buscarReseñasEnPeriodo(self, idVino):
                listaFiltrada.append(vino)
        
        return listaFiltrada

    def calcularPuntajePromedio(cant, sum): #TODO: este metodo va en vino
        prom = sum/cant
        return round(prom, 2)

    def calcularPuntajeDeSommelierEnPeriodo(self, lista): #TODO: CORREGIRLO
        listaRanking = []
        listaReseñas = leerReseñas()

        for vino in lista:
            puntaje = 0
            cantidad = 0
            puntajeGen = 0
            cantGen = 0

            idVino = vino.getId()

            for reseña in listaReseñas:
                if reseña.sosDeVino(idVino) and reseña.esPremium and reseña.validarFechaPeriodo(self.fechaDesde, self.fechaHasta):                   
                    puntaje += reseña.getPuntaje()
                    cantidad += 1

                if reseña.sosDeVino(idVino) and reseña.validarFechaPeriodo(self.fechaDesde, self.fechaHasta):
                    puntajeGen += reseña.getPuntaje()
                    cantGen += 1

                
            
            prom = GestorAdmReporteRanking.calcularPuntajePromedio(cantidad, puntaje)
            promGen = GestorAdmReporteRanking.calcularPuntajePromedio(cantGen, puntajeGen)

            lista = [vino.getDatosVino(), prom, promGen]
            listaRanking.append(lista)
        return listaRanking
    
    def ordenarVinos(self, listaRanking): #TODO: ojo que puede estar bien, OJO B)
        
        listaOrdenada = sorted(listaRanking, key=lambda x: x[1], reverse=True)
        return listaOrdenada[:10]
    
    def opcionGenerarRankingDeVinos(req): #TODO: CORREGIRLO, puede estar bien igual, o no
        fechaDesde, fechaHasta = GestorAdmReporteRanking.tomarFechasReseñas(req)
        tipoReseña = GestorAdmReporteRanking.tomarTipoReseña(req)
        tipoVisualizacion = GestorAdmReporteRanking.tomarTipoVisualizacion(req)
        listaOrdenada = GestorAdmReporteRanking.tomarConfirmacionReporte(fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion)
        return listaOrdenada
        
    def tomarConfirmacionReporte(fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion): #TODO: AFUEEERAAA, igual revisar primero
        gr = GestorAdmReporteRanking(fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion)
        lista = gr.buscarVinosReseñasEnPeriodo()
    
        listaRanking = gr.calcularPuntajeDeSommelierEnPeriodo(lista)
    
        listaOrdenada = gr.ordenarVinos(listaRanking)
        return listaOrdenada

