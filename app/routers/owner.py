from fastapi import APIRouter, Security

from app.database import Session
from app.models import Owner
from app.schemas.owner import Owner as Response_Owner
from app.schemas.owner import OwnerCreate
from app.security import validate_jwt

router = APIRouter()


@router.post("/owner", summary="Request a owner", response_model=Response_Owner)
def add_owner(owner: OwnerCreate) -> Response_Owner:
    with Session() as db:
        db_owner = Owner(**owner.dict())
        db.add(db_owner)
        db.commit()
        db.refresh(db_owner)
        return db_owner


@router.get("/owners/{owner_id}", dependencies=[Security(validate_jwt)], summary="Get owner by id", response_model=Response_Owner)
def get_owner(owner_id: int) -> Response_Owner:
    with Session() as db:
        return db.query(Owner).filter(Owner.id == owner_id).first()


@router.get("/owners", dependencies=[Security(validate_jwt)], summary="Get all owner", response_model=list[Response_Owner])
def get_owners():
    with Session() as db:
        return db.query(Owner).all()


@router.put("/owners/{owner_id}/update", dependencies=[Security(validate_jwt)], summary="Update owner")
def update_owner(owner_id: int, owner: OwnerCreate) -> Response_Owner:
    with Session() as db:
        db_owner = db.query(Owner).filter(Owner.id == owner_id)
        db_owner.update(owner.dict())
        return db_owner.first()
