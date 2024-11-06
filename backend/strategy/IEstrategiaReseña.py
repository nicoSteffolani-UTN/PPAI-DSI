from abc import ABC, abstractmethod
from typing import Tuple, List
from modelos.Vino import Vino

class IEstrategiaReseña(ABC):
    
    @abstractmethod
    def calcularRanking(fechaDesde, fechaHasta, listaVinos) -> List[Tuple[Vino, float, float]]:
        pass
    
    @abstractmethod
    def buscarVinosReseñasEnPeriodo(fechaDesde, fechaHasta, tipoRes, vino) -> List[Vino]: 
        pass

    @abstractmethod
    def calcularPuntajeEnPeriodo(fechaDesde, fechaHasta, tipoRes, listaVinosFiltrados) -> List[Tuple[Vino, float, float]]:
        pass