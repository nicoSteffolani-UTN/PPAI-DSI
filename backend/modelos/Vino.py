class Vino:
    def __init__(self, añada, fechaActualizacion, imagenEtiqueta, nombre, precio, varietal, bodega, reseñas):
        self.__añada = añada
        self.__fechaActualizacion = fechaActualizacion
        self.__imagenEtiqueta = imagenEtiqueta
        self.__nombre = nombre
        self.__precio = precio
        self.__varietal = varietal
        self.__bodega = bodega
        self.__resenias = reseñas


    def __str__(self):
        return (f"{self.__añada} -- {self.__fechaActualizacion} -\
- {self.__imagenEtiqueta} -- {self.__nombre} -- {self.__precio} -\
- {self.__bodega} -- {self.__varietal} -- {self.__resenias}")

    # Getters

    def getAñada(self):
        return self.__añada

    def getFechaActualizacion(self):
        return self.__fechaActualizacion

    def getImagenEtiqueta(self):
        return self.__imagenEtiqueta

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def getBodega(self):
        return self.__resenias

    def getVarietal(self):
        return self.__varietal
    
    def getBodega(self):
        return self.__bodega
    
    def getResenias(self):
        return self.__resenias
    
    # Setters

    def setAñada(self, añada):
        self.__añada = añada

    def setFechaActualizacion(self, fechaActualizacion):
        self.__fechaActualizacion = fechaActualizacion

    def setImagenEtiqueta(self, imagenEtiqueta):
        self.__imagenEtiqueta = imagenEtiqueta

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPrecio(self, precio):
        self.__precio = precio

    def setBodega(self, resenias):
        self.__resenias = resenias

    def setVarietal(self, varietal):
        self.__varietal = varietal

    def setBodega(self, bodega):
        self.__bodega = bodega

    def setResenias(self, resenias):
        self.__resenias = resenias

    def agregarResenia(self, resenia):
        self.__resenias.append(resenia)

    # Methods

    def tenesResenasDeTipoEnPeriodo(self, tipo, fechaInicio, fechaFin):
        pass

    def buscarInfoBodega(self):
        nombreBodega = self.__bodega.getNombre()
        region, pais = self.__bodega.obtenerRegionYPais()

    def buscarVarietal(self):
        pass

    def calcularPuntajeSommelierEnPeriodo(self, fechaInicio, fechaFin):
        pass

    def calcularPuntajePromedio(self):
        pass
    

