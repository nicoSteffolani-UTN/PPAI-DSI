import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from backend.strategy.EstrategiaReseñaSommelier import EstrategiaReseñaSommelier
from backend.strategy.EstrategiaReseñaAmigo import EstrategiaReseñaAmigo
from backend.strategy.EstrategiaReseñaNormal import EstrategiaReseñaNormal
from backend.InterfazExcel import InterfazExcel

class GestorAdmReporteRanking():

    def __init__(self, listaVinos, listaProvincias, listaPaises):
        self.__fechaDesde = ''
        self.__fechaHasta = ''
        self.__tipoRes = ''
        self.__tipoVis = ''
        self.__listaVinos = listaVinos
        self.__listaReseñas = []
        self.__listaVarietales = []
        self.__listaRegiones = []
        self.__listaProvincias = listaProvincias
        self.__listaPaises = listaPaises
        self.__listaBodegas = []
        
        
    def tomarFechasReseñas(self, req):
        fechaDesde = req.get('fechaDesde')
        fechaHasta = req.get('fechaHasta')
        return fechaDesde, fechaHasta
    
    def tomarTipoReseña(self, req):
        tipoReseña = req.get('tipoReseña')
        return tipoReseña
    
    def tomarTipoVisualizacion(self, req):
        tipoVisualizacion = req.get('tipoVisualizacion')
        return tipoVisualizacion

    def opcionGenerarRankingDeVinos(self, req): #TODO: CORREGIRLO, puede estar bien igual, o no
        fechaDesde, fechaHasta = self.tomarFechasReseñas(req)
        self.__fechaDesde = fechaDesde
        self.__fechaHasta = fechaHasta
        tipoReseña = self.tomarTipoReseña(req)
        self.__tipoRes = tipoReseña
        tipoVisualizacion = self.tomarTipoVisualizacion(req)
        self.__tipoVis = tipoVisualizacion
        listaOrdenada = self.crearEstrategia()
        if tipoVisualizacion == 'Excel':
            interfaz = InterfazExcel()
            interfaz.exportarExcel(listaOrdenada)
        return listaOrdenada
    
    def ordenarVinos(self, listaCompleta):
        
        listaOrdenada = sorted(listaCompleta, key=lambda x: x[1], reverse=True)
        return listaOrdenada[:10]

    def crearEstrategia(self):
        if self.__tipoRes == 'sommelier':
            estrategia =  EstrategiaReseñaSommelier()
        elif self.__tipoRes == 'amigos':
            estrategia = EstrategiaReseñaAmigo()
        else:
            estrategia = EstrategiaReseñaNormal()

        return self.calcularRanking(estrategia)


    def calcularRanking(self, estrategia):
        listafiltradaConPuntajes = estrategia.calcularRanking(self.__fechaDesde, self.__fechaHasta, self.__listaVinos)
        listaCompleta = self.tomarDatosVinos(listafiltradaConPuntajes)
        return self.ordenarVinos(listaCompleta)


    def tomarDatosVinos(self, listaFiltradaConPuntajes):

        listaCompleta = []

        for (vino,puntajeTipo,puntajeNorm) in listaFiltradaConPuntajes:
                nombre = vino.getNombre()
                precio = vino.getPrecio()
                bodega, region, pais = vino.buscarInfoBodega(self.__listaProvincias, self.__listaPaises)
                varietal = vino.buscarVarietal()

                listaCompleta.append((nombre, puntajeTipo, puntajeNorm, precio, bodega, varietal, region, pais))

        return listaCompleta
    