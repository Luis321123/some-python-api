from sqlalchemy.orm import Session

from app.settings import get_settings
from app.auth.config import get_hash_password
from app.auth.controller import auth
from app.models.Countries import Countries
from app.seeders import countries
from app.models.Roles import Rol
from app.seeders.role import Role 
from app.services.role import role as role_services
from app.services import serviceUser
from app.schemas.user import UserCreate

settings = get_settings()

def init_db(db: Session) -> None:
# Create all country in BD for data.json
    data_country = countries.data
    country = db.query(Countries).where(Countries.name == data_country[0]['name']).first()
    if not country:
        for item_country in data_country:
            country = Countries(name=item_country['name'], code=item_country['code'])
            db.add(country)
            db.commit()
            db.refresh(country)

# Create Role If They Don't Exist
    member_role = role_services.get_by_name(db=db, name=Role.MEMBER["name"])
    if not member_role:
        user_role_in = Rol(
            name=Role.CONSUMER["name"], description=Role.CONSUMER["description"]
        )   
        role_services.create(db, obj_in=user_role_in)

    admin_role = role_services.get_by_name(db=db, name=Role.ADMINISTRATOR["name"])
    if not admin_role:
        admin_role_in = Rol(
            name=Role.ADMINISTRATOR["name"],
            description=Role.ADMINISTRATOR["description"],
        )
        role_services.create(db, obj_in=admin_role_in)

# Create super user admin test
    # user_current = auth.get_by_email(db=db, email=settings.FIRST_ADMIN_EMAIL)
    # if not user_current:
    #     admin_role = role_services.get_by_name(db=db, name=Role.ADMINISTRATOR["name"])
    #     user_in = UserCreate(
    #         name=settings.FIRST_ADMIN_ACCOUNT_NAME,
    #         lastname=settings.FIRST_ADMIN_ACCOUNT_LASTNAME,
    #         email=settings.FIRST_ADMIN_EMAIL,
    #         password=get_hash_password(settings.FIRST_ADMIN_PASSWORD),
    #         active=True,
    #         roles_id=admin_role.id
    #     )
    #     serviceUser.create(db=db, obj_in=user_in)