from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.order. models import OrderModel, OrderItemModel
from src.cart.models import CartModel
from src.utils.db import get_db
from sqlalchemy.exc import SQLAlchemyError
from src.product.models import ProductModel
from src.order.dtos import OrderSchema, OrderResponseSchemas, UpdateOrderSchema


def create_order(user_id: int, db: Session):
    # Fetch cart items for the user
    cart_items = db.query(CartModel).filter(CartModel.user_id == user_id).all()
    
    if not cart_items:
        raise HTTPException(status_code=404, detail="Cart is empty for this user")

    total_amount = 0

    for item in cart_items:
        product = db.query(ProductModel).filter(ProductModel.id == item.product_id).first()

        total_amount += product.price * item.quantity

    order = OrderModel(
        user_id=user_id,
        total_amount=total_amount,
        status="pending"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in cart_items:
        product = db.query(ProductModel).filter(ProductModel.id == item.product_id).first()

        order_item = OrderItemModel(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price
        )
        db.add(order_item)

    db.commit()
    return order

def get_all_orders(db: Session):
    orders = db.query(OrderModel).all()
    return orders


def get_order_by_id(order_id: int, db: Session):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update_order_status(order_id:int,body:UpdateOrderSchema,db:Session):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if  not order:
        raise HTTPException(404,detail="Order not found")
    order.status = body.status
    db.commit()
    db.refresh(order)
    return order
    

    
    