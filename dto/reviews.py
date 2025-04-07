from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import DateTime


class ReviewDto(BaseModel):
    id: int
    product_name: str
    category_name: str
    rating: Optional[float]
    review_count: int

    date_reviewed: Optional[datetime]
    message: Optional[str]
    user_id: Optional[int]
