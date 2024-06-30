from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.db import get_async_session

from .schemas import UserCreate, UserRead, EmailRead
from .models import User
from .service import read_emails_mail_ru, create, get

router = APIRouter()


# user
@router.get("/")
async def read_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    r = await session.execute(query)
    return r.scalars().all()


@router.post("/")
async def create_user(user_in: UserCreate):
    user = await create(user_in)
    return f'User {user.login} successfully created'


# email
# ! Here we are just testing the functionality of retrieving messages from mail,
# so there is access to any user's data. In a real project
# everything is done via authorization and current_user
@router.get("/{user_login}/mail_ru", response_model=list[EmailRead])
async def read_user_emails_mail_ru(user_login: str):
    """
    Read all emails from mail.ru
    """
    user = await get(user_login)
    return read_emails_mail_ru(user)
