from fastapi import FastAPI

from controllers import product_reviews, products, categories

app = FastAPI()

app.include_router(product_reviews.router)
app.include_router(products.router)

app.include_router(categories.router)
