class Varietal:
    def __init__(self, descripcion, porcent_comp):
        self.descripcion = descripcion
        self.porcent_comp = porcent_comp

    def __str__(self):
        return f"{self.descripcion} - {self.porcent_comp}"
    
    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self, descripcion):    
        self.descripcion = descripcion  

    def getPorcenComp(self):
        return self.porcent_comp
    
    def setPorcenComp(self, porcent_comp):
        self.porcent_comp = porcent_comp

    def toDict(self):
        return {
            "descripcion": self.descripcion,
            "porcent_comp": self.porcent_comp
        }