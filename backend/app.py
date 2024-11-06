import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from flask_cors import CORS

from GestorRanking import GestorAdmReporteRanking
from data.iniciadorBaseDeDatos import IniciarBase

app = Flask(__name__, template_folder='frontend/')
CORS(app, origins=['http://127.0.0.1:8000'])

@app.route('/')
def index():
    req = request.args
    listaVinos, listaProvincia, listaPais = IniciarBase.iniciarBaseDeDatos()
    gestor = GestorAdmReporteRanking(listaVinos, listaProvincia, listaPais)
    listaOrdenada = gestor.opcionGenerarRankingDeVinos(req)
    return listaOrdenada

if __name__ == '__main__':
    app.run(port=5000, debug=True)


