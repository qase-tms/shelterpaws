from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from backend.database.metadata import DeclarativeBase
from backend.settings import Settings


class AnimalPhoto(DeclarativeBase):
    __tablename__ = "animal_photo"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    url = Column(String, nullable=False)

    animal_id = Column(Integer, ForeignKey('animal.id', ondelete="CASCADE"), nullable=False, index=True)

    @hybrid_property
    def full_url(self):
        settings = Settings()
        url = f"{settings.URL_PHOTO_DOWNLOAD}/{self.url}"
        return url
