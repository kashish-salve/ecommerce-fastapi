from sqlalchemy import Column,String,Integer,Float
from src.utils.db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src.order.models import OrderModel


class PaymentModel(Base):
    __tablename__ = "payments"
    
    id = Column(Integer,primary_key=True)
    order_id = Column(Integer,ForeignKey("orders.id"))
    amount = Column(Float)
    payment_status =  Column(String,)
    payment_id = Column(String,nullable=True)
    
    order = relationship("OrderModel",back_populates="payments")