from data.lectorReseña import LectorReseñas
from data.lectorVarietal import LectorVarietal
from data.lectorRegionVitivinicola import LectorRegionVitivinicola
from data.lectorProvincia import LectorProvincias
from data.lectorPaises import LectorPaises
from data.lectorBodegas import LectorBodegas
from data.lectorVinos import LectorVinos


class IniciarBase():

    def iniciarBaseDeDatos(): 
        lectorReseñas = LectorReseñas()
        listaReseñas = lectorReseñas.leerReseñas()

        lectorVarietal = LectorVarietal()
        listaVarietales = lectorVarietal.leerReseñas()
        
        lectorRegiones = LectorRegionVitivinicola()
        listaRegiones = lectorRegiones.leerRegiones()

        lectorProvinicas = LectorProvincias()
        listaProvincias = lectorProvinicas.leerProvincias(listaRegiones)

        lectorPaises = LectorPaises()
        listaPaises = lectorPaises.leerPaises(listaProvincias)

        lectorBodegas = LectorBodegas()
        listaBodegas = lectorBodegas.leerBodegas(listaRegiones)

        lectorVinos = LectorVinos()
        listaVinos = lectorVinos.leerVinos(listaBodegas, listaVarietales, listaReseñas)

        return listaVinos, listaProvincias, listaPaises