import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.lectorReseña import LectorReseñas
from data.lectorVarietal import LectorVarietal
from data.lectorBodegas import LectorBodegas
from data.lectorVinos import LectorVinos
from data.lectorPaises import LectorPaises
from data.lectorRegionVitivinicola import LectorRegionVitivinicola
from data.lectorReseña import LectorReseñas
from data.lectorProvincia import LectorProvincias
from backend.strategy.EstrategiaReseñaSommelier import EstrategiaReseñaSommelier
from backend.strategy.EstrategiaReseñaAmigo import EstrategiaReseñaAmigo
from backend.strategy.EstrategiaReseñaNormal import EstrategiaReseñaNormal

class GestorAdmReporteRanking():
    
    def __init__(self, fechaDesde, fechaHasta, tipoReseña, tipoVisualizacion, listaVinos, listaReseñas, listaVarietales, listaRegiones, listaProvincias, listaPaises, listaBodegas):
        self.__fechaDesde = fechaDesde
        self.__fechaHasta = fechaHasta
        self.__tipoRes = tipoReseña
        self.__tipoVis = tipoVisualizacion
        self.__listaVinos = listaVinos
        self.__listaReseñas = listaReseñas
        self.__listaVarietales = listaVarietales
        self.__listaRegiones = listaRegiones
        self.__listaProvincias = listaProvincias
        self.__listaPaises = listaPaises
        self.__listaBodegas = listaBodegas
        
        
    def tomarFechasReseñas(req):
        fechaDesde = req.get('fechaDesde')
        fechaHasta = req.get('fechaHasta')
        return fechaDesde, fechaHasta
    
    def tomarTipoReseña(self, req):
        tipoReseña = req.get('tipoReseña')

        self.crearEstrategia(tipoReseña)

        return tipoReseña
    
    def tomarTipoVisualizacion(req):
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
        listaOrdenada = self.crearEstrategia(tipoReseña)
    
    def ordenarVinos(self, listaCompleta):
        
        listaOrdenada = sorted(listaCompleta, key=lambda x: x[1], reverse=True)
        return listaOrdenada[:10]
    
   
    def iniciarBaseDeDatos(): 
        lectorReseñas = LectorReseñas()
        listaReseñas = lectorReseñas.leerReseñas()

        lectorVarietal = LectorVarietal()
        listaVarietales = lectorVarietal.leerReseñas()
        
        lectorRegiones = LectorRegionVitivinicola()
        listaRegiones = lectorRegiones.leerRegiones()

        lectorProvinicas = LectorProvincias()
        listaProvincias = lectorProvinicas.leerProvincias(listaRegiones)

        lectorPaises = LectorPaises()
        listaPaises = lectorPaises.leerPaises(listaProvincias)

        lectorBodegas = LectorBodegas()
        listaBodegas = lectorBodegas.leerBodegas(listaRegiones)

        lectorVinos = LectorVinos()
        listaVinos = lectorVinos.leerVinos(listaBodegas, listaVarietales, listaReseñas)

        return listaVinos, listaReseñas, listaVarietales, listaRegiones, listaProvincias, listaPaises, listaBodegas
        

    def crearEstrategia(self):
        if self.__tipoReseña == 'sommelier':
            estrategia =  EstrategiaReseñaSommelier()
        elif self.__tipoReseña == 'amigos':
            estrategia = EstrategiaReseñaAmigo()
        else:
            estrategia = EstrategiaReseñaNormal()

        self.calcularRanking(estrategia)


    def calcularRanking(self, estrategia):
        listafiltradaConPuntajes = estrategia.calcularRanking(self.__fechaDesde, self.__fechaHasta, self.__listaVinos)
        listaCompleta = self.tomarDatosVinos(listafiltradaConPuntajes)
        self.ordenarVinos(listaCompleta)


    def tomarDatosVinos(self, listaFiltradaConPuntajes):

        listaCompleta = []

        for (vino,puntajeTipo,puntajeNorm) in listaFiltradaConPuntajes:
                nombre = vino.getNombre()
                precio = vino.getPrecio()
                bodega, region, pais = vino.buscarInfoBodega(self.__listaProvincias, self.__listaPaises)
                varietal = vino.buscarVarietal()

                listaCompleta.append((nombre, puntajeTipo, puntajeNorm, precio, bodega, varietal, region, pais))

        return listaCompleta
    

if __name__ == '__main__':
    gestor = GestorAdmReporteRanking()
    listaVinos, listaReseñas, listaVarietales, listaRegiones, listaProvincias, listaPaises, listaBodegas = gestor.iniciarBaseDeDatos()
    gestor.tomarFechasReseñas()
    gestor.tomarTipoReseña()
    gestor.tomarTipoVisualizacion()
    gestor.crearEstrategia()
    gestor.calcularRanking()
    gestor.ordenarVinos()
    gestor.tomarDatosVinos()