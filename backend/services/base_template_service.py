from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession as Session


class BaseTemplateService:
    templates = Jinja2Templates(directory="./backend/templates")

    def __init__(self, request: Request, session: Session | None):
        self.request = request
        self.session = session
