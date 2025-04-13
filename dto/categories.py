from typing import Optional

from pydantic import BaseModel


class AddCategoryReq(BaseModel):
    name: str


class AddCategoryRes(AddCategoryReq):
    id: int

class CategoryDto(BaseModel):
    name: str
    id: int



