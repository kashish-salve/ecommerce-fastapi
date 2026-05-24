from pydantic import BaseModel
from typing import List

class ProductSchema(BaseModel):
    name:str
    description:str
    price:float



class ProductListResponse(BaseModel):
    status: str
    total: int
    page: int
    limit: int
    data: List[ProductResponse]

    class Config:
        from_attributes = True
        
class ProductResponse(BaseModel):
    id: int
    name:str
    description:str
    price:float

    class Config:
        from_attributes = True        