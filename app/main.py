from fastapi import FastAPI, Request, Security

from app import models
from app.routers import application, owner, pet
from app.security import validate_jwt

from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", summary="API Info", tags=["Info"])
def read_root(request: Request):
    return {
        "doc": f"{request.url}docs",
        "redoc": f"{request.url}redoc",
        "json": f"{request.url}json",
    }


app.include_router(
    application.router,
    tags=["Application"],
    dependencies=[Security(validate_jwt)]
)
app.include_router(
    owner.router,
    tags=["Owner"],
    dependencies=[Security(validate_jwt)]
)
app.include_router(
    pet.router,
    tags=["Pet"],
    dependencies=[Security(validate_jwt)]
)
