from sqlalchemy.orm import Session

from app.core.settings import get_settings
from app.core.security import get_hash_password
from app.controller.auth import auth
from app.models.Countries import Countries
from app.seeders import countries
from app.models.Roles import Roles
from app.seeders.role import Role 
from app.controller.user import user as user_controller
from app.services.role import role as role_services
from app.services.user import user
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
        user_role_in = Roles(
            name=Role.MEMBER["name"]
        )   
        role_services.create(db, obj_in=user_role_in)

    admin_role = role_services.get_by_name(db=db, name=Role.ADMINISTRATOR["name"])
    if not admin_role:
        admin_role_in = Roles(
            name=Role.ADMINISTRATOR["name"]
        )
        role_services.create(db, obj_in=admin_role_in)

# Create super user admin test
    # user_current = auth.get_by_email(db=db, email=settings.FIRST_ADMIN_EMAIL)
    # if not user_current:
    #       user_in = UserCreate(
             
    #     )
    # user_controller.create(db=db, obj_in=user_in)  