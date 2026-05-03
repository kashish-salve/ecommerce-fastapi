from pydantic import BaseModel

class ProductSchema(BaseModel):
    name:str
    description:str
    price:float

class ProductResponse(BaseModel):
    id:int
    name:str
    description:str
    price:float   