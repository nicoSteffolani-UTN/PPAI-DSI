class Vino:
    def __init__(self, añada, fechaActualizacion, imagenEtiqueta, nombre, precio, varietal, bodega):
        self.__añada = añada
        self.__fechaActualizacion = fechaActualizacion
        self.__imagenEtiqueta = imagenEtiqueta
        self.__nombre = nombre
        self.__precio = precio
        self.__varietal = varietal
        self.__bodega = bodega


    def __str__(self):
        return (f"{self.__añada} -- {self.__fechaActualizacion} -\
- {self.__imagenEtiqueta} -- {self.__nombre} -- {self.__precio} -\
- {self.__bodega} -- {self.__varietal}")

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

    def tenesResenasDeTipoEnPeriodo(self, tipo, fechaInicio, fechaFin):
        pass

    def buscarInfoBodega(self):
        pass

    def buscarVarietal(self):
        pass

    def calcularPuntajeSommelierEnPeriodo(self, fechaInicio, fechaFin):
        pass

    def calcularPuntajePromedio(self):
        pass
    

    def getDatosVino(self): #TODO: AFUEERAAAA
        return {
            "añada": self.getAñada(),
            "fechaActualizacion": self.getFechaActualizacion(),
            "imagenEtiqueta": self.getImagenEtiqueta(),
            "nombre": self.getNombre(),
            "precio": self.getPrecio(),
            "varietal": self.__varietal.getDatosVarietal()
        }

