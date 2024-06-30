from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from backend.src.config import settings
from backend.src.get_emails.router import read_user_emails_mail_ru

router = APIRouter()

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@router.get("/emails/{user_login}", response_class=HTMLResponse)
def get_base_page(request: Request, emails=Depends(read_user_emails_mail_ru)):
    return templates.TemplateResponse("index.html", {"request": request, "emails": emails})
