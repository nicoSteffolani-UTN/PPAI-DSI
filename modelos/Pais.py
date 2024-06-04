class Pais:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDatosPais(self):
        return {
            "nombre": self.nombre
        }

