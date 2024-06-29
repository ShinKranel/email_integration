from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.db import Base


class User(Base):
    __tablename__ = 'user'

    login: Mapped[str] = mapped_column(
        primary_key=True, unique=True, nullable=False
    )
    password: Mapped[str]

    emails = relationship('Email', back_populates='user')


class Email(Base):
    __tablename__ = 'email'

    id: Mapped[str] = mapped_column(primary_key=True)
    email_theme: Mapped[str]
    send_date: Mapped[datetime]
    receive_date: Mapped[datetime]
    email_text: Mapped[str]
    attached_files: Mapped[ARRAY] = mapped_column(ARRAY(String))

    user_id: Mapped[str] = mapped_column(
        ForeignKey('user.login', ondelete='CASCADE'), nullable=False
    )
    user = relationship('User', back_populates='emails')
