from fastapi import HTTPException

from backend.src.db import async_session_maker
from backend.src.get_emails.models import User
from backend.src.get_emails.schemas import UserCreate


async def get_user(user_in: UserCreate) -> User:
    async with async_session_maker() as session:
        user = await session.get(User, user_in.login)
        return user


async def create(user_in: UserCreate) -> User:
    async with async_session_maker() as session:
        user = await get_user(user_in)
        if user:
            raise HTTPException(status_code=400, detail="User already exist")
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
