from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from backend.settings import Settings
from backend.database.metadata import DeclarativeBase


class Animal(DeclarativeBase):
    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name_ru = Column(String, nullable=False)
    name_en = Column(String, nullable=False)
    type = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    age = Column(String, nullable=False)
    size = Column(String, nullable=False)
    photos = relationship(
        "AnimalPhoto",
        back_populates="animal",
        primaryjoin="AnimalPhoto.animal_id == Animal.id",
        lazy="joined",
    )

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
        
