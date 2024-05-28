class Provincia:

    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f'{self.nombre} -- {self.pais}'
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):    
        self.nombre = nombre

    def getPais(self):
        return self.pais
    
    def setPais(self, pais):
        self.pais = pais