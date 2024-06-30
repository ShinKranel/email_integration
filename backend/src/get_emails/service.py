import base64
import email
import imaplib
from datetime import datetime
from email.header import decode_header

from fastapi import HTTPException

from backend.src.db import async_session_maker
from backend.src.get_emails.models import User, Email
from backend.src.get_emails.schemas import UserCreate


async def get(user_login: str) -> User:
    async with async_session_maker() as session:
        user = await session.get(User, user_login)
        return user


async def create(user_in: UserCreate) -> User:
    async with async_session_maker() as session:
        user = await get(user_in.login)
        if user:
            raise HTTPException(status_code=400, detail="User already exist")
        user = User(**user_in.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


# emails
def connection(user: User):
    imap = imaplib.IMAP4_SSL("imap.mail.ru")
    status, result = imap.login(f"{user.login}@mail.ru", user.mail_ru_pass)
    if status == "OK":
        return imap
    else:
        return False


def read_emails_mail_ru(user: User):
    """
    get user emails from mail.ru
    """
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    imap = connection(user)
    if not imap:
        raise HTTPException(status_code=404, detail="mail.ru account not found")

    imap.select("INBOX")
    emails_uid = imap.uid('search', "ALL")[1][0].split()

    emails = list()

    for uid in emails_uid:
        res, msg = imap.uid('fetch', uid, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])

        # get sender's email
        send_from = msg["X-Sender"]

        # get date from mail.ru and delete "day of week" and the last value in str
        receive_date = ' '.join(msg["Date"].split()[1:-1])

        # convert str to datetime
        receive_date_time = datetime.strptime(receive_date, "%d %b %Y %H:%M:%S")

        # get email header
        email_header = decode_header(msg["Subject"])[0][0].decode()

        # get email text
        # email_text = msg.get_payload()[0].get_payload(decode=True)
        email_text = ''
        for part in msg.walk():
            if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                decode_text = base64.b64decode(part.get_payload()).decode()
                email_text = decode_text[:-289]

        user_email = Email(
            id=uid,
            send_from=send_from,
            email_header=email_header,
            receive_date=receive_date_time,
            email_text=email_text,
            attached_files=None
        )

        emails.append(user_email)

    return emails
