from flask import Flask, render_template
from time import sleep
import numpy as np
import cv2
import nltk
from nltk.chat.util import Chat

# Rules for chat
rules = [
    (r"hello", ["hi", "hello"]),
    (r"ac is not working", ["pankha chalao", "sorry i cant control weather"])
]
cb = Chat(rules)
#################-------------images---------------#################


# face descriptor
fd = cv2.CascadeClassifier(cv2.data.haarcascades +
                           'haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while False:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(img_gray, 1.1, 5)
        for x1, y1, w, h in faces:
            cv2.rectangle(img, pt1=(x1, y1), pt2=(x1+w, y1+h),
                          color=tuple(np.random.randint(
                              size=3, low=0, high=255, dtype='int').tolist()),
                          thickness=6)
        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('x'):  # ctrl + Enter for ord 10
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()


app = Flask(__name__)


@app.route('/')
def some_funcion():
    print("hello hi kya hal hai")
    return "hii"


@app.route('/chat')
def some_funcion2():
    return render_template('mypage.html')


@app.route('/images')
def some_funcion3():
    return render_template('home.html')


app.run(debug=True)
