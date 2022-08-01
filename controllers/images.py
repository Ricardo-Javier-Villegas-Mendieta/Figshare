from numpy import rint
import pandas as pd
from flask.json import dump, load
from itertools import chain
from . import db


persona  = pd.read_csv("https://raw.githubusercontent.com/Ricardo-Javier-Villegas-Mendieta/Figshare/main/data.csv")





def get_data():
    return persona

def get_test():
    test = persona.sample(10)
    return test

def guardar_datos(datos):
    db.registrar_Respuesta(datos[0],datos[1],datos[2],datos[3],datos[4])

