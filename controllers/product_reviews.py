from typing import List

from fastapi import APIRouter

from dto.reviews import RatingDto
from services.reviews_service import RevService

router = APIRouter(tags=["product_reviews"], prefix="/api/product_reviews")

@router.get('/')
async def get_product_reviews(service: RevService) -> List[RatingDto]:
    reviews = service.get_reviews()
    return reviews