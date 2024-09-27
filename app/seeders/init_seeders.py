from sqlalchemy.orm import Session

from app.core.settings import get_settings
from app.core.security import hash_password
from app.models import Cities, Regions
from app.models.Countries import Countries
from app.schemas.user import UserCreate
from app.seeders import countries
from app.seeders import regions
from app.seeders import cities
from app.models.Roles import Roles
from app.seeders.role import Role
from app.controller.user import user as user_controller
from app.services.role import role as role_services

settings = get_settings()

def init_db(db: Session) -> None:
# Create all cities in BD for data.json
    data_city = cities.data
    city = db.query(Cities).where(Cities.name == data_city[0]['name']).first()
    if not city:
        for item_city in data_city:
            city = Cities(name=item_city['name'])
            db.add(city)
            db.commit()
            db.refresh(city)

# Create all regions in BD for data.json
    data_region = regions.data
    region = db.query(Regions).where(Regions.name == data_region[0]['name']).first()
    if not region:
        for item_region in data_region:
            region = Regions(name=item_region['name'])
            db.add(region)
            db.commit()
            db.refresh(region)

# Create all country in BD for data.json
    data_country = countries.data
    country = db.query(Countries).where(Countries.name == data_country[0]['name']).first()
    if not country:
        for item_country in data_country:
            country = Countries(name=item_country['name'])
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
    user_in = UserCreate(
        name=settings.FIRST_ADMIN_ACCOUNT_NAME,
        last_name=settings.FIRST_ADMIN_ACCOUNT_NAME,
        email=settings.FIRST_ADMIN_EMAIL,
        password=hash_password(settings.FIRST_ADMIN_PASSWORD),
        is_superuser=True,
        address="test",
        phone="1241414",
        gender="male"
    )
    user_controller.create(db=db, obj_in=user_in)  