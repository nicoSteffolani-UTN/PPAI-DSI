from flask import Flask, render_template, request
from flask_cors import CORS
from GestorRanking import GestorAdmReporteRanking

app = Flask(__name__, template_folder='frontend/')
CORS(app, origins=['http://0.0.0.0:8000'])

@app.route('/')
def index():

    fechaDesde = request.args.get('fechaDesde')
    fechaHasta = request.args.get('fechaHasta')

    gr = GestorAdmReporteRanking(fechaDesde, fechaHasta, 'sommelier', 'tabla')
    lista = gr.buscarVinosReseñasEnPeriodo()

    listaRanking = gr.calcularPuntajeDeSommelierEnPeriodo(lista)

    listaOrdenada = gr.ordenarVinos(listaRanking)

    return listaOrdenada

if __name__ == '__main__':
    app.run(port=5000, debug=True)


