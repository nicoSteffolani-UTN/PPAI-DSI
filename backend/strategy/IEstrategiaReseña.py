from abc import ABC, abstractmethod
from typing import Tuple, List
from modelos.Vino import Vino
from modelos.Reseña import Reseña

class IEstrategiaReseña(ABC):
    
    @abstractmethod
    def calcularRanking(fechaDesde, fechaHasta, tipoRes, listaVinos) -> List[Tuple(Vino, float, float, str, str)]:
        pass
    
    @abstractmethod
    def buscarVinosReseñasEnPeriodo(fechaDesde, fechaHasta, tipoRes, vino) -> List[Vino]: #esto puede cambiar
        pass

    @abstractmethod
    def calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, tipoRes, listaVinosFiltrados) -> float:
        pass