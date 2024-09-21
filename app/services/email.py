from fastapi import BackgroundTasks
from app.core.email import send_email
from app.core.settings import get_settings
from app.models.User import User

settings = get_settings()

async def send_password_reset_email(user: User, background_tasks: BackgroundTasks):
    from app.core.security import hash_password
    string_context = user.get_context_string(context="PASSWORD-TEST")
    token = hash_password(string_context)
    reset_url = f"{settings.FRONTEND_HOST}/resetear?token={token}&email={user.email}"
    data = {
        'app_name': settings.APP_NAME,
        "name": user.name,
        'activate_url': reset_url,
    }
    subject = f"Reinicio de contraseña - {settings.APP_NAME}"
    await send_email(
        recipients=[user.email],
        subject=subject,
        template_name="password-reset.html",
        context=data,
        background_tasks=background_tasks
    )