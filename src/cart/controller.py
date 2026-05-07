from sqlalchemy.orm import Session
from src.cart.models import CartModel
from src.cart.dtos import CartSchema
from fastapi import HTTPException


def add_to_cart(body:CartSchema,db:Session):
    cart_item =db.query(CartModel).filter(
        CartModel.user_id == body.user_id,
        CartModel.product_id == body.product_id).first()
    if cart_item:
        cart_item.quantity += body.quantity

        db.commit()
        db.refresh(cart_item)
        return cart_item
    
    new_item = CartModel(
        user_id=body.user_id,
        product_id= body.product_id,
        quantity=body.quantity
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_cart(user_id:int,db:Session):
    items = db.query(CartModel).filter(CartModel.user_id == user_id).all()
    result =[]
    for item in items:
        product = item.product

        result.append({
            "product_name": product.name,
            "price": product.price,
            "quantity": item.quantity,
            "total":product.price*item.quantity
        })

    
    
    return result


def delete_cart_item(cart_id:int,db:Session):
    item = db.query(CartModel).filter(CartModel.id == cart_id).first()
    if not item:
        raise HTTPException(404,detail="Item not found")
    
    db.delete(item)
    db.commit()
    return{"message":"Item deleted"}


def update_cart(cart_id:int,quantity:int,db:Session):
    item = db.query(CartModel).filter(CartModel.id == cart_id).first()
    if not item:
        raise HTTPException(404,detail="Item not found")
    
    item.quantity = quantity
    db.commit()
    db.refresh(item)
    return item