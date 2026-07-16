from pydantic import BaseModel


class UpdateSettingsSchema(BaseModel):

    dark_mode: bool = False

    notifications_enabled: bool = True

    start_week_on_monday: bool = True