import fastapi
from fastapi_authkit import (
    OAuthApp,
    AuthSetting,
    AuthProviders,
)
from fastapi_authkit.utils import jwt

fake_db = {}
SECRET_KEY = "This is a secret key"


class AuthLogic(AuthProviders.IAuthLogic):
    header: dict[str, str] = {"alg": "HS256"}

    async def login(
        self, userinfo: AuthProviders.UserInfoModel
    ) -> AuthProviders.Token | None:
        if userinfo.name in fake_db:
            return AuthProviders.Token(
                jwt.encode(
                    header=self.header,
                    key=SECRET_KEY,
                    payload=userinfo.dict(),
                ).decode()
            )

    async def singup(self, userinfo: AuthProviders.UserInfoModel) -> None:
        global fake_db
        fake_db[userinfo.name] = userinfo


app: fastapi.FastAPI = fastapi.FastAPI()
auth_router: fastapi.APIRouter = fastapi.APIRouter(prefix="/auth")
auth_app: OAuthApp = OAuthApp(app=app, secret_key=SECRET_KEY)
auth_vias: AuthProviders.AuthVia = AuthProviders.AuthVia(
    oapp=auth_app.oauth,
    vias=(
        AuthSetting(
            name="google",
            client_id="{{client-id}}",
            client_secret="{{client-secret}}",
            client_kwargs=dict(scope="openid profile"),
        )
    ),
)
auth_logic: AuthLogic = AuthLogic()
AuthProviders.GoogleAuthenticationMethod(
    router=auth_router,
    oauth_app=auth_app,
    auth_vias=auth_vias,
    auth_logic=auth_logic,
)