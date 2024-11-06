class Bodega:
    def __init__(self, nombre, descripcion, historia, coordenadas, region):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__historia = historia
        self.__coordenadas = coordenadas
        self.__region = region

    def __str__(self):
        return f'{self.__nombre} -- {self.__descripcion} -- {self.__historia} -- {self.__coordenadas} -- {self.__region}'

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getHistoria(self):
        return self.__historia

    def setHistoria(self, historia):
        self.__historia = historia

    def getCoordenadas(self):
        return self.__coordenadas

    def setCoordenadas(self, coordenadas):
        self.__coordenadas = coordenadas

    def getRegion(self):
        return self.__region

    def setregion(self, region):
        self.__region = region

    def obtenerRegionYPais(self, listaProvincias, listaPaises): 
        nombreRegion = self.__region.getNombre()
        pais = self.__region.obtenerPais(listaProvincias, listaPaises)
        return nombreRegion, pais
    
