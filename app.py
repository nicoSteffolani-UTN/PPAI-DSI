from flask import Flask, render_template
from data.dataVinos.lectorReseña import leerReseñas

app = Flask(__name__, template_folder='frontend/')

@app.route('/')
def index():
    return 'texto prueba'

if __name__ == '__main__':
    listaVinos = leerReseñas()
    for vino in listaVinos:
        print(vino)
    app.run(port=5000, debug=True)


