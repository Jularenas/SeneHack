

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

def getUsersRT(category):
    if(category is None):
        category=''
    db = firestore.client()
    users_ref = db.collection(u'RT')
    docs = users_ref.where(u'categoria',u'==',category).get()
    unificados=[]
    for doc in docs:
        data={}
        user=doc.to_dict()
        print(user)
        data['origen']={}
        data['origen']['longitud']=user['longitudInicial']
        data['origen']['latitud']=user['latitudInicial']
        data['destino']={}
        data['destino']['longitud']=user['longitudFinal']
        data['destino']['latitud']=user['latitudFinal']
        data['usuario']=user['usuario']
        data['categoria']=user['categoria']
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
    data['usuario']="/datosPersonales/"+login
    data['categoria']=categoria
    db = firestore.client()
    user_ref=db.collection(u'RT')
    data['id']=user_ref.where(u'usuario',u'==',data['usuario']).get()[0].id
    print(data)
    db.collection(u'RT').document().set(data)

updateUserRT({'longitud':0,'latitud':0},{'longitud':0,'latitud':0},'datosPersonales/julian','cicla')
def register(user):
    if(user.get('usuario') is None or user.get('passwd') is None or
    user.get('celular') is None or user.get('nombre') is None):
        return str(False)
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
    if(user.get('usuario') is None or user.get('password') is None):
        return str(False)
    usuario=user['usuario']
    passwd=user['passwd'].encode('utf-8')
    m = hashlib.md5()
    m.update(passwd)
    print(m.hexdigest())
    passwd=m.hexdigest()
    db = firestore.client()
    print ("TEST")
    doc_ref=db.collection(u'datosPersonales').document(usuario)
    data={}
    data["usuario"]=usuario
    db.collection(u'RT').document().set(data)
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

def deleteUserRT(username):
    db = firestore.client()
    docs=db.collection(u'RT').where(u'usuario',u'==',u'/datosPersonales/'+username).get()
    print(docs)
    for doc in docs:
        print(doc)
        id=doc.get().id
        print(id)
        db.collection(u'RT').document(id).delete()

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
deleteUserRT('julian')




