from sqlalchemy import Column,Integer,FLOAT,String
from src.utils.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src.user.models import UserModel
from src.product.models import ProductModel

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    total_amount = Column(FLOAT)
    status = Column(String,default="pending")
    user = relationship("UserModel", back_populates="orders")
    items = relationship("OrderItemModel", back_populates="order")


class OrderItemModel(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer,primary_key=True,index=True)
    order_id = Column(Integer,ForeignKey("orders.id"))
    product_id = Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(FLOAT)

    order = relationship("OrderModel", back_populates="items")
