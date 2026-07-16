from pydantic import BaseModel


class CreateNotificationSchema(BaseModel):
    message: str