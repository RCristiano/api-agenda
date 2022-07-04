from pydantic import BaseModel


class PetCreate(BaseModel):
    id: int
    owner_id: int
    Name: str
    birth: str
    species: str


class Pet(PetCreate):
    id: int

    class Config:
        orm_mode = True
