from typing import List, Optional

from fastapi import APIRouter, Path, HTTPException

from custom_exceptions.custom_not_found import CustomNotFound
from dto.products import AddProductReq, ProductDto, ProductWithReviews
from dto.reviews import RatingDto
from services.products_service import ProdService
from services.reviews_service import RevService

router = APIRouter(tags=["products"], prefix="/api/products")

@router.get('/')
async def get_products(service: ProdService) -> List[ProductDto]:
    products = service.get_products()
    return products

@router.get('/{product_id}')
async def get_product(service: ProdService, product_id: int) -> ProductWithReviews:
    data =  service.get_product(product_id)
    return data


@router.post('/')
async def add_product(service: ProdService, req: AddProductReq):
    product = service.add_product(req)
    return product