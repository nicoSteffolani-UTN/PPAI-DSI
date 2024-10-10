class Pais:

    def __init__(self, nombre, provincias):
        self.__nombre = nombre
        self.__provincias = provincias

    def __str__(self):
        return self.__nombre, self.__provincias
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getprovincias(self):
        return self.__provincias
    
    def setprovincias(self, provincias):
        self.__provincias = provincias

    def agregarPais(self, pais):
        self.__provincias.append(pais)

    def contarprovincias(self):
        return len(self.__provincias)

    def getDatosPais(self):
        return {
            "nombre": self.__nombre,
            "provincias": self.__provincias
        }

