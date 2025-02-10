from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/abc')
def abc():
    return render_template("abc.html")


@app.route('/alfa')
def alfa():
    return render_template("alfa.html")


@app.route('/azb')
def azb():
    return render_template("azb.html")


@app.route('/heb')
def heb():
    return render_template("heb.html")


if __name__ == '__main__':
    app.run(debug=True)
