from flask import (
    Flask, render_template,
    redirect, request,
    flash, session,
    jsonify
)

from utils.forms import (
    LoginForm, SignUpForm,
    AddNoteForm, AddTagForm,
    ChangeEmailForm, ChangePasswordForm
)

from flask_restful import Resource, Api, reqparse
from utils.decorators import login_required
from flask_pagedown import PageDown
from flask import Markup
import utils.functions as functions
import firebase
import datetime
import markdown
import random
import json
from flask_cors import CORS
#import utils.seleniumTest 

app = Flask(__name__)
api = Api(app)
CORS(app)
pagedown = PageDown(app)
parser = reqparse.RequestParser()
app.secret_key = str(random.randint(1, 20))
cant = 0
user=None

@app.route('/')
def home_page():
    '''
        App for hompage
    '''
    return 'HelloHack'


@app.route('/login',methods=['POST'])
def login():
    if(request.method=='POST'):
        req_data=request.get_json()
        a=firebase.login(req_data)
        print(a)
        return a
    
@app.route('/register',methods=['POST'])
def register():
    if(request.method=='POST'):
        req_data=request.get_json()
        return firebase.register(req_data)

@app.route('/adyacentes', methods=['POST'])
def adyacentes():
    if(request.method=='POST'):
        req_data=request.get_json(force=True)
        origenLat=req_data['origen']['latitud']
        origenLon=req_data['origen']['longitud']
        destinoLat=req_data['destino']['latitud']
        destinoLon=req_data['destino']['longitud']
        radioSalida=req_data['radioSalida']
        radioLlegada=req_data['radioLlegada']
        user=req_data['user']
        origen={'latitud':origenLat,'longitud':origenLon}
        destino={'latitud':destinoLat,'longitud':destinoLon}
        firebase.createUser(origen,destino,user)		
    return str(functions.get10NearToRadius(origen,destino,radioSalida,radioLlegada,firebase.getUsers()))

@app.route('/adyacentesRT/<category>', methods=['POST'])
def adyacentesRT(category):
    if(request.method=='POST'):
        req_data=request.get_json(force=True)
        origenLat=req_data['origen']['latitud']
        origenLon=req_data['origen']['longitud']
        destinoLat=req_data['destino']['latitud']
        destinoLon=req_data['destino']['longitud']
        radioSalida=req_data['radioSalida']
        radioLlegada=req_data['radioLlegada']
        user=req_data['user']
        origen={'latitud':origenLat,'longitud':origenLon}
        destino={'latitud':destinoLat,'longitud':destinoLon}
        firebase.updateUserRT(origen,destino,user,category)		
    return str(functions.get10NearToRadiusRT(origen,destino,radioSalida,radioLlegada,firebase.getUsersRT(category)))

@app.route('/closed/<user>', methods=['DELETE'])
def close(user):
    if(request.method=='DELETE'):
        print('Conexión cerrada con: '+str(user))
        firebase.deleteUserRT(user)
    return "OK"


    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
