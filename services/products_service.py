from datetime import datetime
from typing import Annotated

from fastapi import Depends

import models
from dto.products import AddProductReq
from repositories.products_repo import ProductRepo, init_products_repo
from repositories.reviews_repo import ReviewsRepo, init_review_repo


class ProductsService:
    def __init__(self, repo: ProductRepo):
        self.repo = repo


    def get_product(self, product_id):
        data = self.repo.get_by_id(product_id)

        return data

    def get_products(self):
        return self.repo.get_all()

    def add_product(self, req_data: AddProductReq):
        product = models.Product(**req_data.model_dump())
        self.repo.add(product)
        return product


def init_products_service(repo: ProductRepo = Depends(init_products_repo)):
    return ProductsService(repo)


ProdService = Annotated[ProductsService, Depends(init_products_service)]