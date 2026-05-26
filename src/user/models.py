from sqlalchemy import Column,Integer,String
from src.utils.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    username = Column(String,nullable=False)
    email = Column(String,unique=True)
    hash_password = Column(String,nullable=False)
    
    orders = relationship("OrderModel", back_populates="user")