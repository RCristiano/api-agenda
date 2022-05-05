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


class Owner(BaseModel):
    id: int
    name: str
    age: int


@app.get("/owners", dependencies=[Security(validate_jwt)], summary="Get all owners", tags=["Owners"])
def list_owners():
    owner = mimesis.Person()
    return [Owner(id=i, name=owner.full_name(), age=owner.age()) for i in range(1, 5)]


@app.get("/owners/{owner_id}", dependencies=[Security(validate_jwt)], summary="Get Owner", tags=["Owner"])
def get_owner(owner_id: int):
    fake = mimesis.Person()
    return Owner(id=owner_id, name=fake.full_name(), age=fake.age())
