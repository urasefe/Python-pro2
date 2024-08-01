from flask import Flask
import random
app = Flask(__name__)
from fotoliste import fotolist
from sifreolus import sifre

@app.route('/')
def index():
    return f'''
    <h1>Burası bir deneme alanı</h1>
    <img src="{random.choice(fotolist)}" alt="resm">
    <h2>{yt()}</h2>
    <h3>{sifre(10)}</h3>
    '''

def yt():
    para = random.randint(1,2)
    if para == 1:
        para = "yazı"
    elif para == 2:
        para = "tura"
    return para


app.run(debug=True)