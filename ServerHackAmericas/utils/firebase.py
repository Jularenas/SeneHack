

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("senehack-firebase-adminsdk-lnk8g-1c14912a19.json")
firebase_admin.initialize_app(cred)