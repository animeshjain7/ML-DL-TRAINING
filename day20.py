from flask import Flask
app = Flask(__name__)

@app.route('/')
def some_funcion():
    return "some message from flask"

app.run(debug=True)
