from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.core.database import async_db_session


async def db_getter() -> AsyncGenerator[AsyncSession, None]:

    async with async_db_session() as session:
        async with session.begin():
            yield session