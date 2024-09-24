
import pyrebase

config = {
    "apiKey": "AIzaSyBUDv0iLSP0T5wzrdiLlbtm9Tbo8B0oXG4",
    "authDomain": "sinai-app-iglesias.firebaseapp.com",
    "databaseURL": "https://sinai-app-iglesias-default-rtdb.firebaseio.com/",
    "storageBucket": "gs://sinai-app-iglesias.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
