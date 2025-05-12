from datetime import datetime
from typing import Annotated

from fastapi import Depends

import models
from dto.reviews import ReviewDto
from repositories.reviews_repo import ReviewsRepo, init_review_repo


class ReviewsService:
    def __init__(self, repo: ReviewsRepo):
        self.repo = repo

    def get_reviews(self):
        return self.repo.get_ratings()

    def remove(self, _id):
        self.repo.remove_rating(_id)
    def add(self, product_id, req_data):
        review = models.Review(**req_data.model_dump())
        review.date_reviewed = datetime.now()
        review.product_id = product_id
        self.repo.add_rating(review)
        return review



def init_reviews_service(repo: ReviewsRepo = Depends(init_review_repo)):
    return ReviewsService(repo)


RevService = Annotated[ReviewsService, Depends(init_reviews_service)]
