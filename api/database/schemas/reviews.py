
from pydantic import BaseModel
from datetime import datetime

class ReviewsCreate(BaseModel):
    user_id:int
    order_id:int
    product_id:int
    rating:int
    review:int
    created_at:datetime

class ReviewsResponse(BaseModel):
    id: int
    user_id:int
    order_id:int
    product_id:int
    rating:int
    review:int
    created_at:datetime


    class Config:
        from_attributes = True

