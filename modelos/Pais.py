class Pais:

    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDatosPais(self):
        return {
            "nombre": self.__nombre
        }

