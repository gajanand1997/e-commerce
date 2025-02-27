

from pydantic import BaseModel
from datetime import datetime

class CartsCreate(BaseModel):
    user_id:int
    product_id:int
    quantity:int
    created_at:datetime

class CartsResponse(BaseModel):
    id: int
    user_id:int
    product_id:int
    quantity:int
    created_at:datetime


    class Config:
        from_attributes = True

