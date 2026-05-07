from fastapi import FastAPI
from src.utils.db import Base,engine
from src.product.routes import product_routes
from src.cart.routes import cart_routes


Base.metadata.create_all(engine)

app = FastAPI(title="This is my Ecommerce_Fastapi Application")

app.include_router(product_routes)
app.include_router(cart_routes)