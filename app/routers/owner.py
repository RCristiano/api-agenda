from fastapi import APIRouter

from app.database import Session
from app.models import Owner
from app.schemas.owner import Owner as Response_Owner
from app.schemas.owner import OwnerCreate

router = APIRouter()


@router.post("/owner", summary="Register a owner", response_model=Response_Owner)
def add_owner(owner: OwnerCreate) -> Response_Owner:
    with Session() as db:
        db_owner = Owner(**owner.dict())
        db.add(db_owner)
        db.commit()
        db.refresh(db_owner)
        return db_owner


@router.get("/owners/{owner_id}", summary="Get owner by id", response_model=Response_Owner)
def get_owner(owner_id: int) -> Response_Owner:
    with Session() as db:
        return db.query(Owner).filter(Owner.id == owner_id).first()


@router.get("/owners", summary="Get all owner", response_model=list[Response_Owner])
def get_owners():
    with Session() as db:
        return db.query(Owner).all()


@router.put("/owners/{owner_id}/update", summary="Update owner")
def update_owner(owner_id: int, owner: OwnerCreate) -> Response_Owner:
    with Session() as db:
        db_owner = db.query(Owner).get(owner_id)
        for key, value in owner:
            if value:
                setattr(db_owner, key, value)
        db.commit()
        db.refresh(db_owner)
        return db_owner
