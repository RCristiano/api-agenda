from fastapi import APIRouter, Security

from app import models
from app.database import Session
from app.schemas.application import Application, ApplicationBase, Status
from app.security import validate_jwt

router = APIRouter()


@router.post("/application", dependencies=[Security(validate_jwt)], summary="Request a application", tags=["Application"])
def submit_application(application: ApplicationBase):
    with Session() as db:
        db_application = models.Application(
            pet_id=application.pet_id, status=application.status, description=application.description)
        db.add(db_application)
        db.refresh(db_application)
        return db_application


@router.get("/applications/{application_id}", dependencies=[Security(validate_jwt)], summary="Get application by id", tags=["Application"])
def get_application(application_id: int):
    with Session() as db:
        return db.query(models.Application).filter(models.Application.id == application_id).first()


@router.get("/applications", dependencies=[Security(validate_jwt)], summary="Get all application", tags=["Application"])
def get_application():
    return Application()


@router.put("/applications/update", dependencies=[Security(validate_jwt)], summary="Update application", tags=["Application"])
def update_application(application: Application) -> Application:
    return application


@router.put("/applications/{application_id}/status_update", dependencies=[Security(validate_jwt)], summary="Update status application", tags=["Application"])
def update_status_application(application_id: int, status: Status) -> Application:
    return Application
