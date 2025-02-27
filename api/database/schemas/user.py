from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: str
    created_at:datetime
    updated_at :datetime

#ye tho wha response body k liye hota hai na iski jrurat nai hai yeha 
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    mob_number: str
    role: str
  

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str
