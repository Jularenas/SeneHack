

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
        data['destino']['latitud']=user['latitudFinal']
        print(data)
        unificados.append(data)
    return unificados

def getUsersRT(category,username):
    if(category is None):
        category='Category'
    db = firestore.client()
    ref = db.collection(u'RT')
    docs = ref.where(u'categoria',u'==',category).get()
    unificados=[]
    for doc in docs:
        data={}
        user=doc.to_dict()
        real_user=db.collection(u'datosPersonales').document(username).get().to_dict()
        print(user)
        print(real_user)
        data['usuario']=doc.id
        print(data['usuario']+" VS "+username)
        if(data['usuario']!=username):
            data['origen']={}
            data['origen']['longitud']=user['longitudInicial']
            data['origen']['latitud']=user['latitudInicial']
            data['destino']={}
            data['destino']['longitud']=user['longitudFinal']
            data['destino']['latitud']=user['latitudFinal']
            data['categoria']=user['categoria']
            data['celular']=real_user['celular']
            print(data)
            unificados.append(data)
    print (unificados)
    return unificados

def createUser(origen,destino,login):
    if(origen is None or destino is None or login is None):
        return
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

def updateUserRT(origen,destino,login,categoria):
    if(origen is None or destino is None or login is None or categoria is None):
        return
    data={}
    data['longitudInicial']=origen['longitud']
    data['latitudInicial']=origen['latitud']
    data['longitudFinal']=destino['longitud']
    data['latitudFinal']=destino['latitud']
    data['categoria']=categoria
    db = firestore.client()
    user_ref=db.collection(u'RT').document(login)
    user_ref.set(data)
    docs=user_ref.get()

def register(user):
    print("sad")
    if(user.get('usuario') is None or user.get('passwd') is None or
    user.get('celular') is None or user.get('nombre') is None):
        return str(False)
    print ("Llega")
    data={}
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    m = hashlib.md5()
    m.update(passwd)
    print ("DIGEST",m.hexdigest(),user)
    data['passwd']=m.hexdigest()
    data['celular']=user['celular']
    data['nombre']=user['nombre']
    db = firestore.client()
    try:
        db.collection(u'datosPersonales').document(usuario).get()
        print ("Ya existe con el usuario")
        return str(False)
    except NotFound:
        db.collection(u'datosPersonales').document(usuario).set(data)
        return str(True)

def login(user):
    print("Inicio",user)
    if(user.get('usuario') is None or user.get('passwd') is None):
        return str(False)
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    print(usuario,passwd)
    m = hashlib.md5()
    m.update(passwd)
    print(m.hexdigest())
    passwd=m.hexdigest()
    db = firestore.client()
    print ("TEST",passwd)
    doc_ref=db.collection(u'datosPersonales').document(usuario)
    data={}
    db.collection(u'RT').document(usuario).set(data)
    try:
        doc=doc_ref.get()
        print(doc)
        print(doc.to_dict())
        if(doc.to_dict()['passwd']!=passwd):
            return str(False)
        return str(True)
    except NotFound:
        return str(False)

def deleteUserRT(username):
    db = firestore.client()
    docs=db.collection(u'RT').document(username).delete()

def testData():
    usuario={}
    usuario['usuario']="test2"
    usuario['nombre']='nombre'
    usuario['passwd']='test'
    usuario['celular']='3017912608'
    print(register(usuario))

    print(login(usuario))
    origen={}
    origen['longitud']=12
    origen['latitud']=12
    destino={}
    destino['longitud']=12
    destino['latitud']=12
    userLogin="test2"
    updateUserRT(origen,destino,userLogin,'cicla')

    origen={}
    origen['longitud']=12
    origen['latitud']=12
    destino={}
    destino['longitud']=12
    destino['latitud']=12
    userLogin="test"
    updateUserRT(origen,destino,userLogin,'cicla')

    getUsersRT('cicla','s.guzmanm')
    getUsersRT('taxi','s.guzmanm')
    getUsersRT('carro','s.guzmanm')

    #deleteUserRT('s.guzmanm')










