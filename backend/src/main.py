from fastapi import FastAPI

from backend.src.config import settings

app = FastAPI(
    title=settings.PROJECT_TITLE
)
