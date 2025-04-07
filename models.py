from typing import List, Optional

from sqlalchemy import Column, DateTime, Float, ForeignKeyConstraint, Index, String, Text, text, Numeric
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = (
        Index('name_UNIQUE', 'name', unique=True),
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(45), nullable=False)

    product: Mapped[List['Product']] = relationship('Product', uselist=True, back_populates='category')


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('username_UNIQUE', 'username', unique=True),
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    username = mapped_column(String(200), nullable=False)
    password = mapped_column(String(255), nullable=False)

    review: Mapped[List['Review']] = relationship('Review', uselist=True, back_populates='user')


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['category.id'], name='fk_product_category'),
        Index('fk_product_category_idx', 'category_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(45), nullable=False)
    price = mapped_column(Numeric(10, 2), nullable=False)
    category_id = mapped_column(INTEGER(11), nullable=False)
    description = mapped_column(Text, nullable=True)

    category: Mapped['Category'] = relationship('Category', back_populates='product')
    review: Mapped[List['Review']] = relationship('Review', uselist=True, back_populates='product')


class Review(Base):
    __tablename__ = 'review'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['product.id'], name='fk_review_product1'),
        ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_review_user1'),
        Index('fk_review_product1_idx', 'product_id'),
        Index('fk_review_user1_idx', 'user_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    rating = mapped_column(Float, nullable=False)
    product_id = mapped_column(INTEGER(11), nullable=False)
    date_reviewed = mapped_column(DateTime, nullable=False)
    message = mapped_column(Text)
    user_id = mapped_column(INTEGER(11))

    product: Mapped['Product'] = relationship('Product', back_populates='review')
    user: Mapped[Optional['User']] = relationship('User', back_populates='review')
