from pydantic import BaseModel
from enum import Enum


class OrderSchema(BaseModel):
    user_id:int
    

class OrderResponseSchemas(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    class Config:
        from_attributes = True  

     
    
class UpdateOrderSchema(BaseModel):
    status: str    
    




class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class OrderStatusUpdateSchema(BaseModel):
    status: OrderStatus  # Automatically validates allowed values only