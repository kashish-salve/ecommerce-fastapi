from sqlalchemy import Column,Integer,String
from src.utils.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    
    orders = relationship("OrderModel", back_populates="user")