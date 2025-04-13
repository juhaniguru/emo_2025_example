from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import DateTime

from dto.users import UserDto


class RatingDto(BaseModel):
    id: int
    product_name: str
    category_name: str
    rating: Optional[float]
    review_count: int

    date_reviewed: Optional[datetime]
    message: Optional[str]
    user_id: Optional[int]

class ReviewDto(BaseModel):
    id: int
    rating: float
    product_id: int
    date_reviewed: datetime
    message: Optional[str]
    user: Optional[UserDto]