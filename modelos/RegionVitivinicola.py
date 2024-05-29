class RegionVitivinicola: 
    def __init__(self, descripcion, nombre, provincia):
        self.descripcion = descripcion
        self.nombre = nombre
        self.provincia = provincia

    def __str__(self):
        return f"{self.descripcion} -- {self.nombre} -- {self.provincia}"
    
    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getProvincia(self):
        return self.provincia
    
    def setProvincia(self, provincia):
        self.provincia = provincia