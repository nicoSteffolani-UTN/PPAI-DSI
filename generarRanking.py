from data.dataVinos.lectorReseña import leerReseñas
from data.dataVinos.lectorVinos import leerVinos

def generarRanking(fechaDesde, fechaHasta, tipoRes, tipoVis):

    listaReseñas = leerReseñas()
    listaFiltrada = []
    listaNormal = []
    for reseña in listaReseñas:
        if reseña.fechaReseña >= fechaDesde and reseña.fechaReseña <= fechaHasta:
            listaNormal.append(reseña)
            if tipoRes == 'sommelier':
                if reseña.esPremium:
                    listaFiltrada.append(reseña)

            elif tipoRes == 'normal':
                listaFiltrada.append(reseña)

            elif tipoRes == 'amigos':
                if not(reseña.esPremium):
                    listaFiltrada.append(reseña)

    f_coincidencias = promedioFiltrado = f_sum_total= 0
    n_coincidencias = promedioNormal = n_sum_total = 0
    listaRanking = []
    listaVinos = leerVinos()
    for vino in listaVinos:
        for reseña in listaFiltrada:
            if vino.id == reseña.vino.id:
                f_coincidencias += 1
                f_sum_total += reseña.puntaje

        for reseña in listaNormal:
            if vino.id == reseña.vino.id:
                n_coincidencias += 1
                n_sum_total += reseña.puntaje


        if f_coincidencias != 0:
            promedioFiltrado = f_sum_total / f_coincidencias
            promedioNormal = n_sum_total / n_coincidencias
            
            lista = [vino, round(promedioFiltrado, 2), round(promedioNormal, 2)]
            listaRanking.append(lista)
        f_coincidencias = n_coincidencias= 0
        f_sum_total= n_sum_total= 0
    listaRanking.sort(key=lambda x: x[1], reverse=True)
    
    for ranking in listaRanking[:10]:
        print(ranking[0].nombre, ' tiene ',ranking[1], ' de promedio', tipoRes,' y ', ranking[2], ' de promedio general.')

generarRanking('2020-01-01', '2021-12-31', 'sommelier', 'tabla')