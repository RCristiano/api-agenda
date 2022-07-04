from fastapi import FastAPI, Request

from app import models
from app.routers import application, owner, pet

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


app.include_router(application.router, tags=["Application"])
app.include_router(owner.router, tags=["Owner"])
app.include_router(pet.router, tags=["Pet"])
# app.include_router(pet.router, tags=["Pet"])
# app.include_router(pet.router, tags=["Pet"])
# app.include_router(pet.router, tags=["Pet"])


# class Chart(BaseModel):
#     id: int
#     pet_id: int
#     # +get_chart(id)
#     # +add_chart(pet_id, vet_id, date, time, description)
#     # +update_chart(id, pet_id, vet_id, date, time, description)


# class Exam(BaseModel):
#     id: int
#     chart_id: int
#     Doctor: str
#     execution_date: datetime
#     type: str
#     file_link: str
#     # +insert(chart_id, Doctor, execution_date, type, file_link)


# class Pathology(BaseModel):
#     id: int
#     chart_id: int
#     description: str
#     # +insert(chart_id, description)
