from pydantic import BaseModel


class CreateTagSchema(BaseModel):
    name: str
    color: str


class TagResponse(BaseModel):
    id: str
    name: str
    color: str

    class Config:
        from_attributes = True