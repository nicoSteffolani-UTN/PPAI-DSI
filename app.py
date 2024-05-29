from flask import Flask, render_template
from data.dataVinos.lectorPaises import leerPaises
from data.dataVinos.lectorBodegas import leerBodegas
import json

app = Flask(__name__, template_folder='frontend/')

@app.route('/')
def index():
    return json.dumps(leerBodegas())

if __name__ == '__main__':
    print(leerBodegas())
    app.run(port=5000, debug=True)

