from typing import List

from fastapi import APIRouter

from dto.categories import AddCategoryReq, AddCategoryRes, CategoryDto
from models import Category
from services.categories_service import CatService

router = APIRouter(tags=["Categories"], prefix="/api/categories")

@router.get('/')
async def get_categories(service: CatService) -> List[CategoryDto]:
    categories = service.get_categories()
    return categories

@router.post('/')
async def add_category(service: CatService, req: AddCategoryReq) -> AddCategoryRes:
    category = service.add_category(req)
    return category