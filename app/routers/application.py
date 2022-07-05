from fastapi import APIRouter

from app.database import Session
from app.models import Application
from app.schemas.application import Application as Response_Application
from app.schemas.application import ApplicationBase, Status

router = APIRouter()


@router.post("/application", summary="Request a application", response_model=Response_Application)
def request_application(owner: ApplicationBase) -> Response_Application:
    with Session() as db:
        db_application = Application(**owner.dict())
        db.add(db_application)
        db.commit()
        db.refresh(db_application)
        return db_application


@router.get("/applications/{application_id}", summary="Get application by id")
def get_application(application_id: int):
    with Session() as db:
        return db.query(Application).filter(Application.id == application_id).first()


@router.get("/applications", summary="Get all application", response_model=list[Response_Application])
def get_application():
    with Session() as db:
        return db.query(Application).all()


@router.put("/applications/{application_id}/update", summary="Update application", response_model=Response_Application)
def update_application(application_id: int, application: ApplicationBase) -> Response_Application:
    with Session() as db:
        db_application = db.query(Application).get(application_id)
        for key, value in application:
            if value:
                setattr(db_application, key, value)
        db.commit()
        db.refresh(db_application)
        return db_application


@router.put("/applications/{application_id}/status_update", summary="Update status application")
def update_status_application(application_id: int, status: Status) -> Application:
    with Session() as db:
        db_application = db.query(Application).get(application_id)
        db_application.status = status
        db.commit()
        db.refresh(db_application)
        return db_application
