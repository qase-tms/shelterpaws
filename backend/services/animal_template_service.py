from fastapi.responses import HTMLResponse
from backend.services.base_template_service import BaseTemplateService


class AnimalTemplateService(BaseTemplateService):
    def __init__(self, request):
        super().__init__(request)

    @staticmethod
    def _complete_template_path(template_name: str):
        return f"pages/index/{template_name}"

    def get_index_template(self) -> HTMLResponse:
        return self.templates.TemplateResponse(
            name=self._complete_template_path("index.html"),
            context={"request": self.request}
        )
