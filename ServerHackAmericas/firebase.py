

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import hashlib


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
    db = firestore.client()
    if(db.collection(u'datosPersonales').document(usuario) is None):
        return
    db.collection(u'datosPersonales').document(usuario).set(data)

def login(user):
    data={}
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    m = hashlib.md5()
    m.update(passwd)
    print(m.hexdigest())
    passwd=m.hexdigest()
    db = firestore.client()
    doc_ref=db.collection(u'datosPersonales').document(usuario)
    if(doc_ref is None):
        return False
    else:
        doc=doc_ref.get()
        print(doc)
        print(doc.to_dict())
        if(doc.to_dict()['passwd']!=passwd):
            return False
    return True

def testData():
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

usuario={}


