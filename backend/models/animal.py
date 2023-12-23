from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.metadata import DeclarativeBase


class Animal(DeclarativeBase):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name_ru = Column(String, nullable=False)
    name_en = Column(String, nullable=False)
