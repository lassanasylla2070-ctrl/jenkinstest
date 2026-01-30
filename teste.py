from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Salut ! Ma mise à jour automatique via Jenkins marche parfaitement ! ✅'

if __name__ == '__main__':
    # On écoute sur 0.0.0.0 pour que ce soit accessible hors du conteneur
    app.run(host='0.0.0.0', port=5000)
