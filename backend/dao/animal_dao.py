from backend.dao.base_dao import BaseDao
from sqlalchemy.ext.asyncio import AsyncSession as Session

from backend.models.animal import Animal


class AnimalDao(BaseDao):

    def __init__(
        self,
        session: Session
    ):
        super().__init__(session, Animal)
