from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session
from backend.src.get_emails.schemas import UserCreate, UserRead
from .models import User

from .service import create

router = APIRouter()


@router.get("/", response_model=list[UserRead])
async def read_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    r = await session.execute(query)
    return r.scalars().all()


@router.post("/")
async def create_user(user_in: UserCreate):
    user = await create(user_in)
    return f'User {user.login} successfully created'
