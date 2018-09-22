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
        if(firebase.login(req_data)):
            global user=req_data['usuario']
            return True
        return False
    
@app.route('/register',methods=['POST'])
def register():
    if(request.method=='POST'):
        req_data=request.get_json()
        if(firebase.login(req_data)):
            global user=req_data['usuario']
            return True
        return firebase.register(req_data)

@app.route('/adyacentes', methods=['POST'])
def adyacentes():
    if(request.method=='POST'):
        req_data=request.get_json()
        origenLat=req_data['origen']['latitud']
        origenLon=req_data['origen']['longitud']
        destinoLat=req_data['destino']['latitud']
        destinoLon=req_data['destino']['longitud']
        radioSalida=req_data['radioSalida']
        radioLlegada=req_data['radioLlegada']
        origen={'latitud':origenLat,'longitud':origenLon}
        destino={'latitud':destinoLat,'longitud':destinoLon}
        firebase.createUser(origen,destino,user)		
    return str(functions.get10NearToRadius(origen,destino,radioSalida,radioLlegada,firebase.getUsers()))


    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
