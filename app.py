import json
from operator import ge
from webbrowser import get
from flask import Flask, render_template, request, flash
import flask
from numpy import imag, indices
from controllers import images
import os

app = Flask(__name__)

app.config.from_mapping(
    HOST=os.environ.get('DATABASE_HOST'),
    USER=os.environ.get('DATABASE_USER'),
    PASSWD=os.environ.get('DATABASE_PASSWORD'),
    BASE=os.environ.get('DATABASE')
)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/instrucciones')
def intro():    
    return render_template('instrucciones.html')


@app.route('/principal')
def principal():
    persona = images.get_test()
    imagen = persona['URL'].tolist()
    id = persona['ID'].tolist()
    return render_template('principal.html', personas = imagen,ids = id)


@app.route('/agradecimiento')
def agradecimiento():
    return render_template('agradecimiento.html')


@app.route('/guardar/<string:respuestas>',methods=['POST'])
def redireccion(respuestas):
    respuestas = json.loads(respuestas)
    for ele in respuestas:
        images.guardar_datos(ele)
    return('/agradecimiento')

if __name__ == '__main__':
    app.run(debug=True)
