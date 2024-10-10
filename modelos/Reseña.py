class Reseña:
    def __init__(self, vino, id, comentario, puntaje, fechaReseña, esPremium):
        self.__id = id
        self.__comentario = comentario
        self.__puntaje = puntaje
        self.__fechaReseña = fechaReseña
        self.__esPremium = esPremium
        self.__vino = vino

    def __str__(self):
        return f'{self.__id} -- {self.__comentario} -- {self.__puntaje} -- {self.__fechaReseña} -- {self.__esPremium} -- {self.__vino}'
    
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getComentario(self):
        return self.__comentario

    def setComentario(self, comentario):
        self.__comentario = comentario

    def getPuntaje(self):
        return self.__puntaje

    def setPuntaje(self, puntaje):
        self.__puntaje = puntaje

    def getFechaReseña(self):
        return self.__fechaReseña

    def setFechaReseña(self, fechaReseña):
        self.__fechaReseña = fechaReseña

    def getEsPremium(self):
        return self.__esPremium

    def setEsPremium(self, esPremium):
        self.__esPremium = esPremium

    def getVino(self):
        return self.__vino

    def setVino(self, vino):
        self.__vino = vino

    def getDatosReseña(self):
        return {
            "id": self.getId(),
            "comentario": self.getComentario(),
            "puntaje": self.getPuntaje(),
            "fechaReseña": self.getFechaReseña(),
            "esPremium": self.getEsPremium(),
            "vino": self.__vino.getDatosVino()
        }
    
    def validarFechaPeriodo(self, fechaDesde, fechaHasta):
        return self.__fechaReseña >= fechaDesde and self.__fechaReseña <= fechaHasta
    
    def sosDeVino(self, idVino):
        if self.__vino.id == idVino:
            return True
