from flask import Flask, render_template, request
from flask_cors import CORS
from GestorRanking import GestorAdmReporteRanking

app = Flask(__name__, template_folder='frontend/')
CORS(app, origins=['http://127.0.0.1:8000'])

@app.route('/')
def index():
    req = request.args
    listaOrdenada = GestorAdmReporteRanking.opcionGenerarRankingDeVinos(req)
    return listaOrdenada

if __name__ == '__main__':
    app.run(port=5000, debug=True)


