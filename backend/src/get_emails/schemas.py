from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    mail_ru_pass: str
    gmail_pass: str
    yandex_pass: str


class UserRead(BaseModel):
    login: str
    mail_ru_pass: str
    gmail_pass: str
    yandex_pass: str


class EmailRead(BaseModel):
    id: str
    send_from: str
    email_header: str
    receive_date: datetime
    email_text: str
    attached_files: list[str] | None
