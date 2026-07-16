from pydantic import BaseModel


class CreateCategorySchema(BaseModel):
    name: str
    color: str = "#2196F3"

class UpdateCategorySchema(BaseModel):
    name: str | None = None
    color: str | None = None
    icon: str | None = None