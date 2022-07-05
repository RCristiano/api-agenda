import enum

from pydantic import BaseModel


class Status(enum.Enum):
    INATIVO = 0
    ATIVO = 1
    EM_ANALISE = 2
    OUTRO = 9


class ApplicationBase(BaseModel):
    pet_id: int | None
    status: Status | None
    description: str | None


class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True
