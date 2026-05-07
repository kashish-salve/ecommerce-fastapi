from fastapi import APIRouter,Depends,status
from src.cart import controller
from src.cart.dtos import CartSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

cart_routes = APIRouter(prefix="/cart",tags=["cart"])

@cart_routes.post("/")
def add(body:CartSchema,db:Session=Depends(get_db)):
    return controller.add_to_cart(body,db)


@cart_routes.get("/{user_id}")
def get(user_id:int,db:Session=Depends(get_db)):
    return controller.get_cart(user_id,db)

@cart_routes.delete("/{cart_id}")
def delete(cart_id:int,db:Session=Depends(get_db)):
    return controller.delete_cart_item(cart_id,db)

@cart_routes.put("/{cart_id}")
def update(cart_id:int,quantity:int,db:Session=Depends(get_db)):
    return controller.update_cart(cart_id,quantity,db)
