from fastapi import APIRouter, Depends
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.order import controller
from src.order.models import OrderModel
from src.order.dtos import OrderSchema,OrderResponseSchemas,UpdateOrderSchema


order_routes = APIRouter(prefix="/orders")


@order_routes.post("/create", response_model=OrderResponseSchemas)
def create_order(body: OrderSchema, db: Session = Depends(get_db)):
    return controller.create_order(body.user_id, db)

@order_routes.get("/all_orders", response_model=list[OrderResponseSchemas])
def get_all_orders(db: Session = Depends(get_db)):
    return controller.get_all_orders(db)

@order_routes.get("/one_order/{order_id}", response_model=OrderResponseSchemas)
def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    return controller.get_order_by_id(order_id, db)

@order_routes.put("/update_status/{order_id}")
def update_order_status(order_id:int,body:UpdateOrderSchema,db:Session=Depends(get_db)):
    return controller.update_order_status(order_id,body,db)