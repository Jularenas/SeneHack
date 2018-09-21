import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
   'apiKey': "AIzaSyCays_2GqFMZivLBi0XMA5lV_vquXNj6yI",
    'authDomain': "senehack.firebaseapp.com",
    'databaseURL': "https://senehack.firebaseio.com",
    'projectId': "senehack",
    'storageBucket': "senehack.appspot.com",
    'messagingSenderId': "194598481712"
})

db = firestore.client()