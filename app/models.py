from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from app.database import Base
from app.schemas.application import Status


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    status = Column(Enum(Status))
    description = Column(String)


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"))
    name = Column(String)
    birth = Column(String)
    species = Column(String)


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(Integer)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
