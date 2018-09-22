

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("C:/Users/Jularenas/Desktop/Hackamericas/SeneHack/ServerHackAmericas/utils/senehack-firebase-adminsdk-lnk8g-fbd99ef620.json")
firebase_admin.initialize_app(cred)

def getUsers():
    db = firestore.client()
    users_ref = db.collection(u'usuarios')
    docs = users_ref.get()
    unificados=[]
    for doc in docs:
        data={}
        user=doc.to_dict()
        print(user)
        data['fechacambio']=str(user['fechacambio'])
        data['origen']={}
        data['origen']['longitud']=user['longitudInicial']
        data['origen']['latitud']=user['latitudInicial']
        data['destino']={}
        data['destino']['longitud']=user['longitudFinal']
        data['destino']['latitud']=user['longitudFinal']
        print(data)
        unificados.append(data)
    return unificados

def createUser(origen,destino):
    data={}
    data['fechacambio']=str(datetime.datetime.now())
    data['longitudInicial']=origen['longitud']
    data['latitudInicial']=origen['latitud']
    data['longitudFinal']=destino['longitud']
    data['latitudFinal']=destino['latitud']
    print(data)
    db = firestore.client()
    db.collection(u'usuarios').document().set(data)