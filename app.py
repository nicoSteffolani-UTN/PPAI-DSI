from flask import Flask, render_template
from data.dataVinos.lectorPaises import leerPaises
import json

app = Flask(__name__, template_folder='frontend/')

@app.route('/')
def index():
    return json.dumps(leerPaises())

if __name__ == '__main__':
    app.run(port=5000, debug=True)

