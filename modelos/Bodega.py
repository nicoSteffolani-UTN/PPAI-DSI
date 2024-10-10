class Bodega:
    def __init__(self, nombre, descripcion, historia, coordenadas, vino):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__historia = historia
        self.__coordenadas = coordenadas
        self.__vinos = vino

    def __str__(self):
        return f'{self.__nombre} -- {self.__descripcion} -- {self.__historia} -- {self.__coordenadas} -- {self.__vinos}'

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

    def getVino(self):
        return self.__vinos

    def setVino(self, vino):
        self.__vinos = vino

    def getDatosBodega(self):
        return {
            "nombre": self.__nombre,
            "descripcion": self.__descripcion,
            "historia": self.__historia,
            "coordenadas": self.__coordenadas,
            "vino": self.__vinos
        }