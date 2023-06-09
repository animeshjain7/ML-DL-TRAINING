from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def some_funcion():
    return render_template('home.html')


app.run(debug=True)
