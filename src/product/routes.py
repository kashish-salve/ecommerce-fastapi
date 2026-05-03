from fastapi import APIRouter,Depends,Query,status
from src.product import controller
from src.product.dtos import ProductSchema,ProductResponse
from src.utils.db import get_db
from sqlalchemy.orm import Session

product_routes = APIRouter(prefix="/products")


@product_routes.post("/create", response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def create_product(body:ProductSchema,db:Session=Depends(get_db)):
    return controller.create_product(body,db)


@product_routes.get("/all_product",response_model=ProductResponse,status_code=status.HTTP_200_OK)
def get_all_product(page:int=Query(1,ge=1),
                    limit:int=Query(10,le=50),
                    db:Session=Depends(get_db)):
    return controller.get_product(db,page,limit)

@product_routes.get("/one_product/{product_id}",status_code=status.HTTP_200_OK)
def get_product(product_id:int,db:Session=Depends(get_db)):
    return controller.get_one_product(db,product_id)

