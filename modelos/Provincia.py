class Provincia:

    def __init__(self, nombre, pais):
        self.__nombre = nombre
        self.__pais = pais

    def __str__(self):
        return f'{self.__nombre} -- {self.__pais}'
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):    
        self.__nombre = nombre

    def getPais(self):
        return self.__pais
    
    def setPais(self, pais):
        self.__pais = pais

    def getDatosProvincia(self):
        return {
            "nombre": self.__nombre,
            "pais": self.__pais.getDatosPais()
        }