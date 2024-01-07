from fastapi import Request
from fastapi.templating import Jinja2Templates


class BaseTemplateService:
    templates = Jinja2Templates(directory="./backend/templates")

    def __init__(self, request: Request):
        self.request = request
