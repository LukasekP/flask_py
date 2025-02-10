from flask import Flask, render_template
app = Flask(__name__)

@app.route('/abc')
def index():
    return render_template("index.html")

@app.route('/alfa')
def index():
    return render_template("index.html")

@app.route('/azb')
def index():
    return render_template("index.html")
@app.route('/heb')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run()