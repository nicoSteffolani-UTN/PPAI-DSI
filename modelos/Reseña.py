class Reseña:
    def __init__(self, vino, id, comentario, puntaje, fechaReseña, esPremium):
        self.id = id
        self.comentario = comentario
        self.puntaje = puntaje
        self.fechaReseña = fechaReseña
        self.esPremium = esPremium
        self.vino = vino

    def __str__(self):
        return f'{self.id} -- {self.comentario} -- {self.puntaje} -- {self.fechaReseña} -- {self.esPremium} -- {self.vino}'
    
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getComentario(self):
        return self.comentario

    def setComentario(self, comentario):
        self.comentario = comentario

    def getPuntaje(self):
        return self.puntaje

    def setPuntaje(self, puntaje):
        self.puntaje = puntaje

    def getFechaReseña(self):
        return self.fechaReseña

    def setFechaReseña(self, fechaReseña):
        self.fechaReseña = fechaReseña

    def getEsPremium(self):
        return self.esPremium

    def setEsPremium(self, esPremium):
        self.esPremium = esPremium

    def getVino(self):
        return self.vino

    def setVino(self, vino):
        self.vino = vino

    def getDatosReseña(self):
        return {
            "id": self.getId(),
            "comentario": self.getComentario(),
            "puntaje": self.getPuntaje(),
            "fechaReseña": self.getFechaReseña(),
            "esPremium": self.getEsPremium(),
            "vino": self.vino.getDatosVino()
        }
    
    def validarFechaPeriodo(self, fechaDesde, fechaHasta):
        return self.fechaReseña >= fechaDesde and self.fechaReseña <= fechaHasta
    
    def sosDeVino(self, idVino):
        if self.vino.id == idVino:
            return True
