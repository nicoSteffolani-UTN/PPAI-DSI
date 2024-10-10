class RegionVitivinicola: 
    def __init__(self, nombre, descripcion, bodegas):
        self.__descripcion = descripcion
        self.__nombre = nombre
        self.__bodegas = bodegas

    def __str__(self):
        return f"{self.__nombre} -- {self.__descripcion} -- {self.__bodegas}"
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
      

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
       

    def getBodegas(self):
        return self.__bodegas
    
    def setBodegas(self, bodegas):
        self.__bodegas = bodegas

    def agregarBodega(self, bodega):
        self.__bodegas.append(bodega)

    def contarBodegas(self):
        return len(self.__bodegas)

    def getDatosRegionVitivinicola(self):
        return {
            "nombre": self.__nombre,
            "descripcion": self.__descripcion,
            "bodegas": self.__bodegas
        }