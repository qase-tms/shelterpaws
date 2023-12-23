from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from backend.database.metadata import DeclarativeBase


class Animal(DeclarativeBase):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name_ru = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    photos = relationship('AnimalPhoto', backref='animal', lazy='joined')

    @hybrid_property
    def photo_urls(self):
        return [photo.full_url for photo in self.photos]

    @hybrid_property
    def last_photo(self):
        if len(self.photos) > 0:
            return self.photos[len(self.photos) - 1].full_url
        else:
            return None
