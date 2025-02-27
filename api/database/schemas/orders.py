

from pydantic import BaseModel
from datetime import datetime

class OrdersCreate(BaseModel):
    user_id:int
    subtotal:int
    discount:float
    total:float
    status:str
    shipping_address:str
    updated_at:datetime
    created_at:datetime

class OrdersResponse(BaseModel):
    id: int
    user_id:int
    subtotal:int
    discount:float
    total:float
    status:str
    shipping_address:str
    updated_at:datetime
    created_at:datetime


    class Config:
        from_attributes = True








