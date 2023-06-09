from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def some_funcion():
    return render_template('home.html')


@app.route('/home/<name>')
def some_funcion2(name):
    print(name)
    return render_template(
        'home.html',name_value=name
        )

app.run(debug=True)
