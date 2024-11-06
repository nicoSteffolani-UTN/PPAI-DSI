from strategy.IEstrategiaReseña import IEstrategiaReseña

class EstrategiaReseñaAmigo(IEstrategiaReseña):


    def buscarVinosReseñasEnPeriodo(self, fechaDesde, fechaHasta, listaVinos):
        
        listaVinosFiltrados = []

        for vino in listaVinos:
            
            vinoReseñas = vino.getReseñas()
            for reseña in vinoReseñas:

                esSommelier = reseña.sosDeSommelier()
                sosDePeriodo = reseña.sosDePeriodo(fechaDesde, fechaHasta)

                if  sosDePeriodo and not esSommelier:
                    listaVinosFiltrados.append(vino)
        
        return listaVinosFiltrados

    def calcularPuntajeEnPeriodo(self, fechaDesde, fechaHasta, listaVinosFiltrados):
        
        listaVinosFiltradosConPuntaje = []
        
        for vino in listaVinosFiltrados:

            totalPuntosTipo = 0
            cantReseniasTipo = 0
            totalPuntos = 0
            cantResenias = 0

            reseñas = vino.getReseñas()

            for reseña in reseñas:

                esSommelier = reseña.sosDeSommelier()
                sosDePeriodo = reseña.sosDePeriodo(fechaDesde, fechaHasta)
    
                if sosDePeriodo and not esSommelier:
                    totalPuntosTipo += reseña.getPuntaje()
                    cantReseniasTipo += 1
                if sosDePeriodo:
                    totalPuntos += reseña.getPuntaje()
                    cantResenias += 1

            puntajePromedioTipo = vino.calcularPuntajePromedio(cantReseniasTipo, totalPuntosTipo)
            puntajePromedio = vino.calcularPuntajePromedio(cantResenias, totalPuntos)
            
            listaVinosFiltradosConPuntaje.append((vino, puntajePromedioTipo, puntajePromedio))
        
        return listaVinosFiltradosConPuntaje

    def calcularRanking(self, fechaDesde, fechaHasta, listaVinos):
        listaFiltrada = self.buscarVinosReseñasEnPeriodo(fechaDesde, fechaHasta, listaVinos)
        return self.calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, listaFiltrada)
    
    