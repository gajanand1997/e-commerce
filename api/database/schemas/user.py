from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    mobile: str
    address: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    mobile: str
    address: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str
