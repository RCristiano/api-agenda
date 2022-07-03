from datetime import datetime
from enum import Enum
import os
import mimesis
from fastapi import FastAPI, Request, HTTPException, status
from pydantic import BaseModel

from fastapi import Depends, Security
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from jose import JWTError, jwt

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"


def validate_jwt(
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> dict:
    try:
        return jwt.decode(token.credentials, SECRET_KEY,
                          algorithms=[ALGORITHM])
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e


app = FastAPI()


@app.get("/", summary="API Info", tags=["Info"])
def read_root(request: Request):
    return {
        "doc": f"{request.url}docs",
        "redoc": f"{request.url}redoc",
        "json": f"{request.url}json",
    }


class Status(Enum):
    INATIVO = 0
    ATIVO = 1


class Application(BaseModel):
    id: int
    owner_id: int
    pet_id: int
    status: Status
    description: str
    # +insert_application(pet_id, status, description)
    # +get_application(id)
    # +update_application(id, status, description)
    # +status_update(id, status)


@app.post("/application", summary="Request a application", tags=["Application"])
def submit_application(application: Application):
    return application


@app.get("/applications/{application_id}", dependencies=[Security(validate_jwt)], summary="Get application", tags=["Application"])
def get_application(application_id: int):
    fake = mimesis.Person()
    return Owner(id=application_id, name=fake.full_name(), age=fake.age())


@app.get("/applications", dependencies=[Security(validate_jwt)], summary="Get all application", tags=["Application"])
def get_application():
    fake = mimesis.Person()
    return Owner(id=application_id, name=fake.full_name(), age=fake.age())


class Owner(BaseModel):
    id: int
    cpf: int
    password: str
    Name: str
    Email: str
    Phone: str
    Address: str
    City: str
    # +get_owner(id)
    # +get_pets(id)
    # +add_owner(name, email, phone, address, city)
    # +update_owner(id, name, email, phone, address, city)


@ app.get("/owners", dependencies=[Security(validate_jwt)], summary="Get all owners", tags=["Owner"])
def list_owners():
    owner = mimesis.Person()
    return [Owner(id=i, name=owner.full_name(), age=owner.age()) for i in range(1, 5)]


@ app.get("/owners/{owner_id}", dependencies=[Security(validate_jwt)], summary="Get Owner", tags=["Owner"])
def get_owner(owner_id: int):
    fake = mimesis.Person()
    return Owner(id=owner_id, name=fake.full_name(), age=fake.age())


class Pet(BaseModel):
    id: int
    owner_id: int
    Name: str
    birth: datetime
    species: str
    # +getPet(id)
    # +add_pet(owner_id, name)
    # +update_pet(id, owner_id, name)
    # +get_charts(id)


class Chart(BaseModel):
    id: int
    pet_id: int
    # +get_chart(id)
    # +add_chart(pet_id, vet_id, date, time, description)
    # +update_chart(id, pet_id, vet_id, date, time, description)


class Exam(BaseModel):
    id: int
    chart_id: int
    Doctor: str
    execution_date: datetime
    type: str
    file_link: str
    # +insert(chart_id, Doctor, execution_date, type, file_link)


class Pathology(BaseModel):
    id: int
    chart_id: int
    description: str
    # +insert(chart_id, description)
