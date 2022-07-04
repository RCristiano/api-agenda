from fastapi import APIRouter, Security

from app.database import Session
from app.models import Pet
from app.schemas.pet import Pet as Response_Pet
from app.schemas.pet import PetCreate
from app.security import validate_jwt

router = APIRouter()


@router.post("/pet", summary="Request a pet", response_model=Response_Pet)
def add_pet(pet: PetCreate) -> Response_Pet:
    with Session() as db:
        db_pet = Pet(**pet.dict())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet


@router.get("/pets/{pet_id}", dependencies=[Security(validate_jwt)], summary="Get pet by id", response_model=Response_Pet)
def get_pet(pet_id: int) -> Response_Pet:
    with Session() as db:
        return db.query(Pet).filter(Pet.id == pet_id).first()


@router.get("/pets", dependencies=[Security(validate_jwt)], summary="Get all pet", response_model=list[Response_Pet])
def get_pets():
    with Session() as db:
        return db.query(Pet).all()


@router.put("/pets/{pet_id}/update", dependencies=[Security(validate_jwt)], summary="Update pet")
def update_pet(pet_id: int, pet: PetCreate) -> Response_Pet:
    with Session() as db:
        db_pet = db.query(Pet).filter(Pet.id == pet_id)
        db_pet.update(pet.dict())
        return db_pet.first()
