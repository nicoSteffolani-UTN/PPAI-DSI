from flask import Flask, render_template
from flask_cors import CORS
from generarRanking import GestorRanking

app = Flask(__name__, template_folder='frontend/')
CORS(app)

@app.route('/')
def index():
    gr = GestorRanking('2020-01-01', '2021-12-31', 'sommelier', 'tabla')
    gr.buscarVinosReseñasEnPeriodo()
    lista = gr.calcularPuntajeDeSommelierEnPeriodo()
    listaOrdenada = gr.ordenarVinos(lista)
    return listaOrdenada

if __name__ == '__main__':
    app.run(port=5000, debug=True)


