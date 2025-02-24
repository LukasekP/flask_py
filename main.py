from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret key"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['user'] == '123' and request.form['heslo'] == '123':
            flash("Login successful", "success")
            return redirect(url_for('index'))
        flash("Login unsuccessful", "danger")
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
