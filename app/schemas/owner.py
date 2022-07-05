from pydantic import BaseModel


class OwnerBase(BaseModel):
    cpf: int | None
    name: str | None
    email: str | None
    phone: str | None
    address: str | None
    city: str | None


class OwnerCreate(OwnerBase):
    password: str | None


class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True
