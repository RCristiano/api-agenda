from pydantic import BaseModel


class PetCreate(BaseModel):
    owner_id: int | None
    name: str | None
    birth: str | None
    species: str | None


class Pet(PetCreate):
    id: int

    class Config:
        orm_mode = True
