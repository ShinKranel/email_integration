from fastapi import FastAPI

from backend.src.config import settings
from backend.src.get_emails.router import router as get_emails_router

app = FastAPI(
    title=settings.PROJECT_TITLE
)

app.include_router(get_emails_router, prefix="/get_emails", tags=["get_emails"])
