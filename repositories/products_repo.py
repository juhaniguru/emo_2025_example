from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session, joinedload

import models
from custom_exceptions.custom_not_found import CustomNotFound

from db import connect_to_db


class ProductRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, _id):
        product = self.db.query(models.Product).filter(models.Product.id == _id).first()
        if not product:
            raise CustomNotFound('product not found')
        return product

    def get_all(self):
        return self.db.query(models.Product).all()

    def add(self, _product: models.Product):
        self.db.add(_product)
        self.db.commit()


def init_products_repo(db: Session = Depends(connect_to_db)):
    return ProductRepo(db)
