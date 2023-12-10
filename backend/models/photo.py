from sqlalchemy import Integer, Column, String, ForeignKey
from backend.database.metadata import DeclarativeBase


class Photo(DeclarativeBase):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    url = Column(String, nullable=False)

    animal_id = Column(Integer, ForeignKey('animal.id', ondelete="CASCADE"), nullable=False, index=True)
