<<<<<<< HEAD
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
=======


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("senehack-firebase-adminsdk-lnk8g-1c14912a19.json")
firebase_admin.initialize_app(cred)
>>>>>>> f38e8a0f87d2dc2bf4d275152e847e647beab263
