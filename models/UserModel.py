from pydantic import BaseModel, validator
import re


class UserModel(BaseModel):
    metadata: list
    content_data: list
    username: str
    comment: str
    provider_user_key: str
    email: str
    is_admin: str
    password: str
    name: str
    application_name: str
    user_state: str
    provider_name: str

    @validator('provider_user_key', 'is_admin', 'user_state')
    def must_be_int(cls, v):
        if re.match('^[0-9]*$', v) is None:
            raise ValueError('Must contain only numbers')
        return v.title()
