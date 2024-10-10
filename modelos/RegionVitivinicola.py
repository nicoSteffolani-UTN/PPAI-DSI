class RegionVitivinicola: 
    def __init__(self, descripcion, nombre, provincia):
        self.__descripcion = descripcion
        self.__nombre = nombre
        self.__provincia = provincia

    def __str__(self):
        return f"{self.__descripcion} -- {self.__nombre} -- {self.__provincia}"
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getProvincia(self):
        return self.__provincia
    
    def setProvincia(self, provincia):
        self.__provincia = provincia

    def getDatosRegionVitivinicola(self):
        return {
            "descripcion": self.__descripcion,
            "nombre": self.__nombre,
            "provincia": self.__provincia.getDatosProvincia()
        }