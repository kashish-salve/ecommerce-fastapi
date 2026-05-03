from src.product.dtos import ProductSchema
from sqlalchemy.orm import Session
from src.product.models import ProductModel
from fastapi import HTTPException




def create_product(body:ProductSchema,db:Session):
    data = body.model_dump()
    new_product = ProductModel(name = data["name"],
                               description = data["description"],
                               price = data["price"])
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
    

def get_product(db:Session,page:int,limit:int):
    skip = (page - 1)*limit
    product = db.query(ProductModel).offset(skip).limit(limit).all()
    total = db.query(ProductModel).count()
    return{"status":"all product",
           "total": total,
           "page": page,
           "limit": limit,
           "data": product}

def get_one_product(db: Session, product_id: int):
    one_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not one_product:
        raise HTTPException(404,detail="product id is incorrect")
    return one_product
     