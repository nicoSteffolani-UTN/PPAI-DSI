class Vino:
    def __init__(self, id, añada, fechaActualizacion, imagenEtiqueta, nombre, precio, bodega, varietal):
        self.id = id
        self.añada = añada
        self.fechaActualizacion = fechaActualizacion
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.precio = precio
        self.bodega = bodega
        self.varietal = varietal


    def __str__(self):
        return f"{self.id} -- {self.añada} -- {self.fechaActualizacion} -
        - {self.imagenEtiqueta} -- {self.nombre} -- {self.precio} -
        - {self.bodega} -- {self.varietal}"

    # Getters
    def getId(self):
        return self.id

    def getAñada(self):
        return self.añada

    def getFechaActualizacion(self):
        return self.fechaActualizacion

    def getImagenEtiqueta(self):
        return self.imagenEtiqueta

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getBodega(self):
        return self.bodega

    def getVarietal(self):
        return self.varietal

    # Setters
    def setId(self, id):
        self.id = id

    def setAñada(self, añada):
        self.añada = añada

    def setFechaActualizacion(self, fechaActualizacion):
        self.fechaActualizacion = fechaActualizacion

    def setImagenEtiqueta(self, imagenEtiqueta):
        self.imagenEtiqueta = imagenEtiqueta

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def setBodega(self, bodega):
        self.bodega = bodega

    def setVarietal(self, varietal):
        self.varietal = varietal

    

