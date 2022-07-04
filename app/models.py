from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String

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
    Name = Column(String)
    birth = Column(Date)
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

# class Chart(BaseModel):
#     id: int
#     pet_id: int
#     # +get_chart(id)
#     # +add_chart(pet_id, vet_id, date, time, description)
#     # +update_chart(id, pet_id, vet_id, date, time, description)


# class Exam(BaseModel):
#     id: int
#     chart_id: int
#     Doctor: str
#     execution_date: datetime
#     type: str
#     file_link: str
#     # +insert(chart_id, Doctor, execution_date, type, file_link)


# class Pathology(BaseModel):
#     id: int
#     chart_id: int
#     description: str
#     # +insert(chart_id, description)
