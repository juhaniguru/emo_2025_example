from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

import models
from custom_exceptions.custom_not_found import CustomNotFound
from db import connect_to_db


class ReviewsRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_ratings(self):
        res = self.db.execute(text(
            'SELECT p.id, p.name AS product_name, c.name AS category_name, ROUND(AVG(ra.rating), 1) AS rating, COUNT(ra.product_id) AS review_count, date_reviewed, message, user_id FROM product AS p LEFT JOIN review AS ra ON ra.product_id = p.id INNER JOIN category AS c ON c.id = p.category_id GROUP BY p.id'))
        return res.mappings().all()

    def get_rating_by_id(self, rating_id):
        rating = self.db.query(models.Review).filter(models.Review.id == rating_id).first()
        if rating is None:
            raise CustomNotFound('Review not found')
        return rating

    def remove_rating(self, _id):
        rating = self.get_rating_by_id(_id)
        self.db.delete(rating)
        self.db.commit()
        return None

    def add_rating(self, rating: models.Review):
        self.db.add(rating)
        self.db.commit()

    def get_restaurant(self, _id):
        res = self.db.execute(text(
            'SELECT re.id, name, cuisine, price_range, address, open_status, ROUND(AVG(ra.value), 1) AS rating, COUNT(*) AS review_count FROM restaurant AS re LEFT JOIN rating AS ra ON ra.restaurant_id = re.id WHERE re.id = :reid GROUP BY re.id'),
            {'reid': _id})
        return res.mappings().first()

    def get_ratings_by_restaurant(self, _id):
        res = self.db.execute(text(
            'SELECT ra.id, user_id, value, description, date_rated FROM rating AS ra  WHERE restaurant_id = :reid'),
            {'reid': _id})
        return res.mappings().all()


def init_review_repo(db: Session = Depends(connect_to_db)):
    return ReviewsRepo(db)
