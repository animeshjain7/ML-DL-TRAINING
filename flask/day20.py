import nltk
from nltk.chat.util import Chat


#Rules for chat
rules = [
    (r"hello",["hi","hello"]),
    (r"ac is not working",["pankha chalao","sorry i cant control weather"])
]
cb = Chat(rules)




from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def some_funcion():
    return "hii"

@app.route('/chat')
def some_funcion2():
    return render_template('mypage.html')


app.run(debug=True)
