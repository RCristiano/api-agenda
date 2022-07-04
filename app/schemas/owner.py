from pydantic import BaseModel


class OwnerBase(BaseModel):
    cpf: int
    name: str
    email: str
    phone: str
    address: str
    city: str


class OwnerCreate(OwnerBase):
    password: str


class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True
