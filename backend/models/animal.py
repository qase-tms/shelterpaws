from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from backend.settings import Settings
from backend.database.metadata import DeclarativeBase


class Animal(DeclarativeBase):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name_ru = Column(String, nullable=False)
    name_en = Column(String, nullable=False)

    photos = relationship('AnimalPhoto', backref='animal', lazy='joined')
    type = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    age = Column(String, nullable=False)
    size = Column(String, nullable=False)

    @hybrid_property
    def photo_urls(self):
        return [photo.full_url for photo in self.photos]

    @hybrid_property
    def last_photo(self):
        if len(self.photos) > 0:
            return self.photos[len(self.photos) - 1].full_url
        else:
            return None

    @hybrid_property
    def link(self):
        settings = Settings()
        return f"http://{settings.APP_HOST}:{settings.APP_PORT}/animals/animal/{self.id}"

    @hybrid_property
    def img_src(self):
        return self.photos[0].full_url if self.photos and self.photos[0] else ''

    @hybrid_property
    def name(self):
        return self.name_en
