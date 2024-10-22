class Varietal:
    def __init__(self, descripcion, porcent_comp):
        self.__descripcion = descripcion
        self.__porcent_comp = porcent_comp

    def __str__(self):
        return f"{self.__descripcion} - {self.__porcent_comp}"
    
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):    
        self.__descripcion = descripcion  

    def getPorcenComp(self):
        return self.__porcent_comp
    
    def setPorcenComp(self, porcent_comp):
        self.__porcent_comp = porcent_comp

    def getDatosVarietal(self): #TODO: AFUEEEERAAAAA
        return {
            "descripcion": self.__descripcion,
            "porcent_comp": self.__porcent_comp
        }