from flask import Flask, render_template
from flask_cors import CORS
from GestorRanking import GestorRanking

app = Flask(__name__, template_folder='frontend/')
CORS(app)

@app.route('/')
def index():

    gr = GestorRanking('2020-01-01', '2021-12-31', 'sommelier', 'tabla')
    lista = gr.buscarVinosReseñasEnPeriodo()

    listaRanking = gr.calcularPuntajeDeSommelierEnPeriodo(lista)

    listaOrdenada = gr.ordenarVinos(listaRanking)


    return listaOrdenada

if __name__ == '__main__':
    app.run(port=5000, debug=True)


