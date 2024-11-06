class Reseña:
    def __init__(self, comentario, puntaje, fechaReseña, esPremium):
        self.__comentario = comentario
        self.__puntaje = puntaje
        self.__fechaReseña = fechaReseña
        self.__esPremium = esPremium

    def __str__(self):
        if self.__esPremium:
            return f'{self.__comentario} -- {self.__puntaje} -- {self.__fechaReseña} -- Es Premium'
        else:
            return f'{self.__comentario} -- {self.__puntaje} -- {self.__fechaReseña} -- No es Premium'

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
    
    def sosDePeriodo(self, fechaDesde, fechaHasta): 
        return self.__fechaReseña >= fechaDesde and self.__fechaReseña <= fechaHasta
    
    def sosDeSommelier(self):
        if self.__esPremium:
            return True


    def sosDeVino(self, idVino):
        if self.__vino.id == idVino:
            return True
    
