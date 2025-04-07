from fastapi import Depends
from sqlalchemy.orm import Session

import models
from db import connect_to_db


class CategoriesRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models.Category).all()

    def add(self, category: models.Category):
        self.db.add(category)
        self.db.commit()


def init_categories_repo(db: Session = Depends(connect_to_db)):
    return CategoriesRepo(db)
