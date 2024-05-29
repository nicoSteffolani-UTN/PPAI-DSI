from flask import Flask, render_template
from generarRanking import generarRanking
from flask_cors import CORS

app = Flask(__name__, template_folder='frontend/')
CORS(app)

@app.route('/')
def index():
    return generarRanking('2020-01-01', '2021-12-31', 'sommelier', 'tabla')

if __name__ == '__main__':
    app.run(port=5000, debug=True)


