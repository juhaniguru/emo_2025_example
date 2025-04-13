from typing import Optional, List

from pydantic import BaseModel

from dto.categories import CategoryDto
from dto.reviews import ReviewDto


class AddProductReq(BaseModel):
    name: str
    price: float
    category_id: int
    description: Optional[str] = None


class ProductDto(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    category: CategoryDto


class ProductWithReviews(ProductDto):
    review: List[ReviewDto]


