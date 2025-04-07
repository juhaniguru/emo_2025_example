from datetime import datetime
from typing import Annotated

from fastapi import Depends

import models
from repositories.reviews_repo import ReviewsRepo, init_review_repo


class ReviewsService:
    def __init__(self, repo: ReviewsRepo):
        self.repo = repo

    def get_reviews(self):
        return self.repo.get_ratings()


def init_reviews_service(repo: ReviewsRepo = Depends(init_review_repo)):
    return ReviewsService(repo)


RevService = Annotated[ReviewsService, Depends(init_reviews_service)]
