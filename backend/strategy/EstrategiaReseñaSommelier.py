import IEstrategiaReseña

class EstrategiaReseñaSommelier(IEstrategiaReseña):

    def __init__(self):
        pass
    
    
    def buscarVinosReseñasEnPeriodo(self, fechaDesde, fechaHasta, listaVinos):

        listaVinosFiltrados = []

        for vino in listaVinos:
            
            vinoReseñas = vino.getReseñas()
            for reseña in vinoReseñas:
                if reseña.getTipo() == 'sommelier' and reseña.getFecha() >= fechaDesde and reseña.getFecha() <= fechaHasta:
                    listaVinosFiltrados.append(vino)
        
        self.calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, listaVinosFiltrados)
        

    def calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, listaVinosFiltrados):

        listaVinosFiltradosConPuntaje = []
        
        for vino in listaVinosFiltrados:

            totalPuntosTipo = 0
            cantReseniasTipo = 0
            totalPuntos = 0
            cantResenias = 0

            reseñas = vino.getReseñas()

            for reseña in reseñas:
    
                if reseña.getTipo() == 'sommelier' and reseña.getFecha() >= fechaDesde and reseña.getFecha() <= fechaHasta:
                    totalPuntosTipo += reseña.getPuntaje()
                    cantReseniasTipo += 1
                if reseña.getFecha() >= fechaDesde and reseña.getFecha() <= fechaHasta:
                    totalPuntos += reseña.getPuntaje()
                    cantResenias += 1

            puntajePromedioTipo = vino.calcularPuntajePromedio(cantReseniasTipo, totalPuntosTipo)
            puntajePromedio = vino.calcularPuntajePromedio(cantResenias, totalPuntos)
            
            listaVinosFiltradosConPuntaje.append((vino, puntajePromedioTipo, puntajePromedio))
        
        return listaVinosFiltradosConPuntaje
            

    def calcularRanking(self, fechaDesde, fechaHasta, tipoRes, listaVinos):
        var = self.buscarVinosReseñasEnPeriodo(fechaDesde, fechaHasta, tipoRes, listaVinos)
        self.calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, tipoRes, var)

