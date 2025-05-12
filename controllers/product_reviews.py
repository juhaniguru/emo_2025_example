from typing import List

from fastapi import APIRouter, HTTPException

from custom_exceptions.custom_not_found import CustomNotFound
from dto.reviews import RatingDto, AddReviewDto
from services.reviews_service import RevService

router = APIRouter(tags=["product_reviews"], prefix="/api/product_reviews")


@router.get('/')
async def get_product_reviews(service: RevService) -> List[RatingDto]:
    reviews = service.get_reviews()
    return reviews


@router.delete('/{product_id}/reviews/{review_id}')
async def delete_review(service: RevService, product_id: int, review_id: int):
    try:
        service.remove(review_id)
        return None
    except CustomNotFound:
        raise HTTPException(status_code=404, detail="Review not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/{product_id}/reviews/')
async def create_review(service: RevService, product_id: int, request_data: AddReviewDto):
   review = service.add(product_id, request_data)
   return review

