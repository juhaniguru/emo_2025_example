from fastapi import Depends
from sqlalchemy.orm import Session

import models

from db import connect_to_db


class ProductRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models.Product).all()

    def add(self, product: models.Product):
        self.db.add(product)
        self.db.commit()


def init_products_repo(db: Session = Depends(connect_to_db)):
    return ProductRepo(db)
