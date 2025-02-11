from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import SessionLocal
from api.database.schemas.user import UserResponse
from api.crud import get_user_by_id
from api.token import get_current_user
from api.database.connection import get_db

router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    return current_user
