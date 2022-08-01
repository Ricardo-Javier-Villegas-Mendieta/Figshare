import psycopg2
from flask import current_app

def get_db():
    db = psycopg2.connect(
        host = current_app.config['HOST'],
        user = current_app.config['USER'],
        password = current_app.config['PASSWD'],
        database = current_app.config['BASE']
    )
    c = db.cursor()
    return db,c

def registrar_Respuesta(foto,et,AMp,Ep,Ip):
    try:
        db,c = get_db()
        c.execute("INSERT INTO test values(%s,%s,%s,%s,%s)"
                ,(foto,et,AMp,Ep,Ip))
        db.commit()
        db.close()
        print("REGISTRO EXITOSO")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)