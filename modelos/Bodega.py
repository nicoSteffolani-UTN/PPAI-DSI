class Bodega:
    def __init__(self, nombre, descripcion, historia, coordenadas, region):
        self.nombre = nombre
        self.descripcion = descripcion
        self.historia = historia
        self.coordenadas = coordenadas
        self.region = region

    def __str__(self):
        return f'{self.nombre} -- {self.descripcion} -- {self.historia} -- {self.coordenadas} -- {self.region}'

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getHistoria(self):
        return self.historia

    def setHistoria(self, historia):
        self.historia = historia

    def getCoordenadas(self):
        return self.coordenadas

    def setCoordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def getRegion(self):
        return self.region

    def setRegion(self, region):
        self.region = region

    def toDict(self):
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "historia": self.historia,
            "coordenadas": self.coordenadas,
            "region": self.region.toDict()
        }