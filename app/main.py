from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials


from app.api.api import api_router
from app.core.settings import get_settings
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "firebase-adminsdk-w9a5t@sinai-app-iglesias.iam.gserviceaccount.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

settings = get_settings()

def create_application():
    application = FastAPI(title=settings.APP_NAME,
        version="0.0.1",)
       
    application.include_router(api_router)
    return application

app = create_application()

origins = [
    str(settings.FRONTEND_HOST)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hi, I am Louis - Your app is done & working."}

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("app/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


