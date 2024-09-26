
import pyrebase

from app.core.settings import get_settings

settings = get_settings()

config = {
    "apiKey": settings.FIREBASE_API_KEY,
    "authDomain": settings.FIREBASE_AUTH_DOMAIN,
    "databaseURL": settings.FIREBASE_DATABASE_URL,
    "projectId": settings.FIREBASE_PROJECT_ID,
    "storageBucket": settings.FIREBASE_STORAGE_BUCKET,
    "messagingSenderId": settings.FIREBASE_MESSAGING,
    "appId": settings.FIREBASE_APP_ID
    }
    
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

 