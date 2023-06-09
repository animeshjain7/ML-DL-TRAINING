from flask import Flask
app = Flask(__name__)


@app.route('/')
def some_funcion():
    return '''
    <html>
    <head>
    <title>home</title></head>
    <body>
    <h1>hello !!!!</h1>
    </body>
    </html>
    '''


app.run(debug=True)
