import mimesis
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


@app.get("/", summary="API Info", tags=["Info"])
def read_root(request: Request):
    return {
            "doc": f"{request.url}/docs",
            "redoc": f"{request.url}/redoc",
            "json": f"{request.url}/json"
        }

class Owner(BaseModel):
    id: int
    name: str
    age: int
    
@app.get("/owners", summary="Get all owners", tags=["Owners"])
def list_owners():
    owner = mimesis.Person()
    return [Owner(id=i, name=owner.full_name(), age=owner.age()) for i in range(10)]
    
@app.get("/owners/{owner_id}", summary="Get Owner", tags=["Owner"])
def get_owner(owner_id: int):
    fake = mimesis.Person()
    return Owner(id=owner_id, name=fake.full_name(), age=fake.age())
