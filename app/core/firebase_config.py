
import pyrebase

config = {

     "apiKey": "AIzaSyBUDv0iLSP0T5wzrdiLlbtm9Tbo8B0oXG4",
    "authDomain": "sinai-app-iglesias.firebaseapp.com",
    "databaseURL": "https://sinai-app-iglesias-default-rtdb.firebaseio.com/",
    "projectId": "sinai-app-iglesias",
    "storageBucket": "gs://sinai-app-iglesias.appspot.com",
    "messagingSenderId": "129026009710",
    "appId": "1:129026009710:android:388a3346fad67a22af147f"}
    
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

 