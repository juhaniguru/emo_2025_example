from typing import List

from fastapi import APIRouter

from dto.products import AddProductReq, ProductDto
from services.products_service import ProdService
from services.reviews_service import RevService

router = APIRouter(tags=["products"], prefix="/api/products")

@router.get('/')
async def get_products(service: ProdService) -> List[ProductDto]:
    products = service.get_products()
    return products

@router.post('/')
async def add_product(service: ProdService, req: AddProductReq):
    product = service.add_product(req)
    return product