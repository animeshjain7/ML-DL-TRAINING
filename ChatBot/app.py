import nltk
from nltk.chat.util import Chat

#Rules for chat
rules = [
    (r"hello|hi",["hi","hello"]),
    (r"ac is not working",["pankha chalao","sorry i cant control weather"])
]
cb = Chat(rules)

#######################------FLASK-------################################
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def some_funcion():
    return "hii"

@app.route('/chat' ,methods=['POST','GET'])
def chatBot():
    # res = ""
    if request.method == "POST":
        ques = request.form['ask_me']
        res = cb.respond(ques)
        print(res)  
        return render_template('home.html',response_from_flask = res)
    else:
        return render_template('home.html')
    
app.run(debug=True)
