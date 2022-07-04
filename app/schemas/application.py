import enum

from pydantic import BaseModel


class Status(enum.Enum):
    INATIVO = 0
    ATIVO = 1
    EM_ANALISE = 2
    OUTRO = 9


class ApplicationBase(BaseModel):
    pet_id: int
    status: Status
    description: str


class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True
