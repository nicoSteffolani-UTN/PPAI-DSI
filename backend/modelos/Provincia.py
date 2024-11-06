class Provincia:

    def __init__(self, nombre, regiones):
        self.__nombre = nombre
        self.__regiones = regiones

    def __str__(self):
        return f'{self.__nombre} -- {self.__regiones}'
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):    
        self.__nombre = nombre


    def getRegiones(self):
        return self.__regiones
    
    def setRegiones(self, regiones):
        self.__regiones = regiones

    def agregarRegion(self, region):
        self.__regiones.append(region)

    def contarRegiones(self):
        return len(self.__regiones)
    
    def obtenerPais(self, listaPaises):
        for pais in listaPaises:
            if self in pais.getProvincias():
                nombrePais = pais.getNombre()
                return nombrePais
        return 'La provincia no pertenece a ningun pais'

    def getDatosProvincia(self):
        return {
            "nombre": self.nombre
        }