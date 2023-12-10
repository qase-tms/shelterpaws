from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class PostgresAccessor:
    def __init__(self, db_url: str):
        self.engine = None
        self.session_maker = None
        if not db_url:
            raise ValueError("Expected database url")
        self.DB_URL = db_url

    async def set_engine(self) -> None:
        self.engine = create_async_engine(
            self.DB_URL,
            echo=False
        )
        self.session_maker = sessionmaker(
            bind=self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def stop(self):
        await self.engine.dispose()

    @asynccontextmanager
    async def get_master_session(self):
        async with self.session_maker.begin() as session:  # pylint: disable=no-member
            yield session
