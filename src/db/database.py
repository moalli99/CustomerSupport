from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)


from src.core.config import settings 

DATABASE_URL=settings.database_url

engine=create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal=async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False

)

async def get_db()->AsyncGenerator[AsyncSession,None]:
    async with SessionLocal() as session:
        yield session 