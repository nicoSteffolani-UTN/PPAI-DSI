from strategy.IEstrategiaReseña import IEstrategiaReseña

class EstrategiaReseñaNormal(IEstrategiaReseña):


    def buscarVinosReseñasEnPeriodo(self, fechaDesde, fechaHasta, listaVinos):
        listaVinosFiltrados = []

        for vino in listaVinos:

            vinoReseñas = vino.getReseñas()
            for reseña in vinoReseñas:

                sosDePeriodo = reseña.sosDePeriodo(fechaDesde, fechaHasta)

                if sosDePeriodo:
                    listaVinosFiltrados.append(vino)

        return listaVinosFiltrados


    def calcularPuntajeEnPeriodo(self, fechaDesde, fechaHasta, listaVinosFiltrados):
        
        listaVinosFiltradosConPuntaje = []

        for vino in listaVinosFiltrados:

            totalPuntos = 0
            cantResenias = 0

            reseñas = vino.getReseñas()

            for reseña in reseñas:

                sosDePeriodo = reseña.sosDePeriodo(fechaDesde, fechaHasta)

                if sosDePeriodo:
                    totalPuntos += reseña.getPuntaje()
                    cantResenias += 1

            puntajePromedio = vino.calcularPuntajePromedio(cantResenias, totalPuntos)
            
            listaVinosFiltradosConPuntaje.append((vino, puntajePromedio, puntajePromedio))
        
        return listaVinosFiltradosConPuntaje



    def calcularRanking(self, fechaDesde, fechaHasta, listaVinos):
        listaFiltrada = self.buscarVinosReseñasEnPeriodo(fechaDesde, fechaHasta, listaVinos)
        return self.calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, listaFiltrada)

