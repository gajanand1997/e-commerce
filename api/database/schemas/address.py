
from pydantic import BaseModel
from datetime import datetime

class AAddressCreate(BaseModel):
    user_id:int
    state: str
    city:str
    address_line1:str
    address_line2:str
    pincode:int
    complete_address:str
    created_at:datetime

class AAddressResponse(BaseModel):
    id: int
    user_id:int
    state: str
    city:str
    address_line1:str
    address_line2:str
    pincode:int
    complete_address:str
    created_at:datetime


    class Config:
        from_attributes = True


