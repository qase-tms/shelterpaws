from backend.database.metadata import DeclarativeBase
from sqlalchemy import Integer, Column, String



class Shelter(DeclarativeBase):
    __tablename__ = "shelter"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    slug = Column(String(50), nullable=False)

    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


