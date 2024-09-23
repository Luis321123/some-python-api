
import pyrebase

config = {
    "apiKey": "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyBUDv0iLSP0T5wzrdiLlbtm9Tbo8B0oXG4",
    "authDomain": "sinai-app-iglesias.firebaseapp.com",
    "databaseURL": "https://sinai-app-iglesias-default-rtdb.firebaseio.com/",
    "storageBucket": "sinai-app-iglesias.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("tu_email@example.com", "tu_contraseña")
db = firebase.database()