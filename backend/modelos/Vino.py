class Vino:
    def __init__(self, añada, fechaActualizacion, imagenEtiqueta, nombre, precio, varietal, bodega, reseñas):
        self.__añada = añada
        self.__fechaActualizacion = fechaActualizacion
        self.__imagenEtiqueta = imagenEtiqueta
        self.__nombre = nombre
        self.__precio = precio
        self.__varietal = varietal
        self.__bodega = bodega
        self.__reseñas = reseñas


    def __str__(self):
        return (f"{self.__añada} -- {self.__fechaActualizacion} -\
- {self.__imagenEtiqueta} -- {self.__nombre} -- {self.__precio} -\
- {self.__bodega} -- {self.__varietal} -- {self.__reseñas}")

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
    
    def getReseñas(self):
        return self.__reseñas
    
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

    def setVarietal(self, varietal):
        self.__varietal = varietal

    def setBodega(self, bodega):
        self.__bodega = bodega

    def setReseñas(self, reseñas):
        self.__reseñas = reseñas

    def agregarResenia(self, resenia):
        self.__resenias.append(resenia)

    # Methods

    def tenesResenasDeTipoEnPeriodo(self, tipo, fechaInicio, fechaFin):
        for resenia in self.__resenias:
            if resenia.getTipo() == tipo and resenia.getFecha() >= fechaInicio and resenia.getFecha() <= fechaFin:
                return True

    def buscarInfoBodega(self, listaProvincias, listaPaises):
        nombreBodega = self.__bodega.getNombre()
        region, pais = self.__bodega.obtenerRegionYPais(listaProvincias, listaPaises)
        return nombreBodega, region, pais

    def buscarVarietal(self):
        return self.__varietal.getDescripcion()


    def calcularPuntajePromedio(cant, sum):
        prom = sum/cant
        return round(prom, 2)
    

