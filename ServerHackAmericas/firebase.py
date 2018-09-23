

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import hashlib
import json
from google.cloud.exceptions import NotFound

cred = credentials.Certificate("senehack-firebase-adminsdk-lnk8g-fbd99ef620.json")
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

def createUser(origen,destino,login):
    data={}
    data['fechacambio']=str(datetime.datetime.now())
    data['longitudInicial']=origen['longitud']
    data['latitudInicial']=origen['latitud']
    data['longitudFinal']=destino['longitud']
    data['latitudFinal']=destino['latitud']
    data['usuario']="/datosPersonales/"+login
    print(data)
    db = firestore.client()
    db.collection(u'usuarios').document().set(data)

def register(user):
    data={}
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    m = hashlib.md5()
    m.update(passwd)
    print (m.hexdigest())
    data['passwd']=m.hexdigest()
    data['celular']=user['celular']
    data['nombre']=user['nombre']
    db = firestore.client()
    try:
        db.collection(u'datosPersonales').document(usuario).get()
        return str(False)
    except NotFound:
        db.collection(u'datosPersonales').document(usuario).set(data)
        return str(True)

def login(user):
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    m = hashlib.md5()
    m.update(passwd)
    print(m.hexdigest())
    passwd=m.hexdigest()
    db = firestore.client()
    print ("TEST")
    doc_ref=db.collection(u'datosPersonales').document(usuario)
    try:
        doc = doc_ref.get()
        doc=doc_ref.get()
        print(doc)
        print(doc.to_dict())
        if(doc.to_dict()['passwd']!=passwd):
            return str(False)
        return str(True)
    except NotFound:
        return str(False)

def testData():
    usuario={}
    usuario['usuario']="julian"
    usuario['nombre']='nombre'
    usuario['passwd']='test'
    usuario['celular']='3017912608'
    print(register(usuario))
    usuario['usuario']="s.guzmanm"
    usuario['passwd']='test'
    usuario['celular']='3017912608'
    register(usuario)
    print(login(usuario))
    origen={}
    origen['longitud']=12
    origen['latitud']=12
    destino={}
    destino['longitud']=12
    destino['latitud']=12
    userLogin="s.guzmanm"
    createUser(origen,destino,userLogin)
