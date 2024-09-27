
import firebase_admin
from firebase_admin import credentials, messaging
from app.core.firebase_config import config

cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)


def send_notification(title, content, image, token, data=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=content,
            image=image,
        ),
        data=data,
        tokens=[token],
    )
    res = messaging.send_multicast(message)
    print("notificacion enviada exitosamente:", str(res))
    return res