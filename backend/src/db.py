from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend.src.config import settings

engine = create_engine(settings.DATABASE_URL)
async_engine = create_async_engine(settings.DATABASE_URL_ASYNC)

session_maker = sessionmaker(engine)
async_session_maker = async_sessionmaker(async_engine)


def get_session():
    with session_maker as session:
        yield session


async def get_async_session():
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass
