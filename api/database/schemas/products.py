
from pydantic import BaseModel
from datetime import datetime

class ProductsCreate(BaseModel):
    category_id:int
    name: str
    description:str
    mrp:float
    net_price:float
    quantity_in_stock:int
    image:str
    created_at:datetime
    updated_at:datetime

class ProductsResponse(BaseModel):
    id: int
    category_id:int
    name: str
    description:str
    mrp:float
    net_price:float
    quantity_in_stock:int
    image:str
    created_at:datetime
    updated_at:datetime


    class Config:
        from_attributes = True

