from fastapi.responses import HTMLResponse
from backend.dao.animal_dao import AnimalDao
from backend.models.animal import Animal
from backend.services.base_template_service import BaseTemplateService
from backend.schemas.animal_schemas import AnimalIndexSchema


class AnimalTemplateService(BaseTemplateService):
    def __init__(self, request, session):
        super().__init__(request, session)

    @staticmethod
    def _complete_template_path(template_name: str):
        return f"pages/index/{template_name}"

    async def get_index_template(self) -> HTMLResponse:
        animals: list[Animal] = await AnimalDao(self.session).find_all()
        cards = [AnimalIndexSchema.model_validate(animal) for animal in animals]
        return self.templates.TemplateResponse(
            name=self._complete_template_path("index.html"),
            context={"request": self.request, "cards": cards}
        )
