from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/<jmeno>')
def hello(jmeno):
    return f"<h1>Vítej {jmeno}</h1>"

@app.route('/nasobek/<int:cislo>/<int:cislo2>')
def nasobek(cislo, cislo2):
    vysledek = cislo * cislo2
    return f"Vysledek je {vysledek}"

if __name__ == '__main__':
    app.run()