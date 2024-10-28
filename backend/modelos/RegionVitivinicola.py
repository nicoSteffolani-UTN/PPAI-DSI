class RegionVitivinicola: 
    def __init__(self, nombre, descripcion):
        self.__descripcion = descripcion
        self.__nombre = nombre

    def __str__(self):
        return f"{self.__nombre} -- {self.__descripcion}"
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    
    def obtenerPais(self):
        pass

    def getDatosRegionVitivinicola(self): #TODO: AFUEEEERAAAAA
        return {
            "nombre": self.__nombre,
            "descripcion": self.__descripcion, 
        }