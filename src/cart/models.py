from sqlalchemy import Column,Integer,ForeignKey
from src.utils.db import Base
from sqlalchemy.orm import relationship


class CartModel(Base):
    __tablename__ = "cart"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer)      
    product_id = Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer,default=1)

    product = relationship("ProductModel")
    product = relationship("ProductModel", backref="cart_items")
