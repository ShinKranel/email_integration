from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from backend.src.config import settings
from backend.src.get_emails.router import router as get_emails_router
from backend.src.pages.router import router as pages_router

app = FastAPI(
    title=settings.PROJECT_TITLE
)

app.mount(
    "/static",
    StaticFiles(directory='frontend/static'),
    name="static",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.include_router(get_emails_router, prefix="/get_emails", tags=["get_emails"])
app.include_router(pages_router, tags=["pages"])
