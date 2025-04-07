from datetime import datetime
from typing import Annotated

from fastapi import Depends

import models
from dto.categories import AddCategoryReq
from dto.products import AddProductReq
from repositories.categories_repo import CategoriesRepo, init_categories_repo
from repositories.products_repo import ProductRepo, init_products_repo
from repositories.reviews_repo import ReviewsRepo, init_review_repo


class CategoriesService:
    def __init__(self, repo: CategoriesRepo):
        self.repo = repo

    def get_categories(self):
        return self.repo.get_all()

    def add_category(self, req_data: AddCategoryReq):
        cat = models.Category(**req_data.model_dump())
        self.repo.add(cat)
        return cat


def init_categories_service(repo: CategoriesRepo = Depends(init_categories_repo)):
    return CategoriesService(repo)


CatService = Annotated[CategoriesService, Depends(init_categories_service)]