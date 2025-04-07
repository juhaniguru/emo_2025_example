from typing import Optional

from pydantic import BaseModel


class AddProductReq(BaseModel):
    name: str
    price: float
    category_id: int
    description: Optional[str] = None


class ProductDto(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category_id: int
