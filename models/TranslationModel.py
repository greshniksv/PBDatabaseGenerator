from pydantic import BaseModel, validator
import re
import os.path


class TranslationModel(BaseModel):
    metadata: list
    content_data: list
    language: str
    draft_by: str
    slug: str
    permalink: str
    created_by: str
    allowed_children: str
    title: str
    is_published: str
    file: str

    @validator('language', 'draft_by', 'created_by', 'title', 'is_published')
    def must_be_int(cls, v):
        if re.match('^[0-9]*$', v) is None:
            raise ValueError('Must contain only numbers')
        return v.title()

    @validator('file')
    def must_file_exist(cls, v):
        if os.path.exists(v) is False:
            raise ValueError('Must contain path to existing file')
        return v.title()
