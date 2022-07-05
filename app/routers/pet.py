from fastapi import APIRouter

from app.database import Session
from app.models import Pet
from app.schemas.pet import Pet as Response_Pet
from app.schemas.pet import PetCreate

router = APIRouter()


@router.post("/pet", summary="Register a pet", response_model=Response_Pet)
def add_pet(pet: PetCreate) -> Response_Pet:
    with Session() as db:
        db_pet = Pet(**pet.dict())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet


@router.get("/pets/{pet_id}", summary="Get pet by id", response_model=Response_Pet)
def get_pet(pet_id: int) -> Response_Pet:
    with Session() as db:
        return db.query(Pet).filter(Pet.id == pet_id).first()


@router.get("/pets", summary="Get all pet", response_model=list[Response_Pet])
def get_pets():
    with Session() as db:
        return db.query(Pet).all()


@router.put("/pets/{pet_id}/update", summary="Update pet")
def update_pet(pet_id: int, pet: PetCreate) -> Response_Pet:
    with Session() as db:
        db_pet = db.query(Pet).get(pet_id)
        for key, value in pet:
            if value:
                setattr(db_pet, key, value)
        db.commit()
        db.refresh(db_pet)
        return db_pet
