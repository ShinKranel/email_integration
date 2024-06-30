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
    mail_ru_pass: Mapped[str | None] = None
    gmail_pass: Mapped[str | None] = None
    yandex_pass: Mapped[str | None] = None

    emails = relationship('Email', back_populates='user')


class Email(Base):
    __tablename__ = 'email'

    id: Mapped[str] = mapped_column(primary_key=True)
    send_from: Mapped[str]
    email_header: Mapped[str | None]
    receive_date: Mapped[datetime]
    email_text: Mapped[str]
    attached_files: Mapped[ARRAY | None] = mapped_column(ARRAY(String), default=None)

    user_id: Mapped[str] = mapped_column(
        ForeignKey('user.login', ondelete='CASCADE'), nullable=False
    )
    user = relationship('User', back_populates='emails')
