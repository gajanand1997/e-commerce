from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.categories import CategoryCreate, CategoryResponse
from api.crud.category import create_category,delete_category,get_all_category
from typing import List



# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=CategoryResponse)
def add(category: CategoryCreate, db: Session = Depends(get_db)):
 
    return create_category(db,category)


@router.delete("/delete/{category_id}", response_model=dict)
def delete(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)



@router.get("/all_category", response_model=List[CategoryResponse])
def list_category(db: Session = Depends(get_db)):
    return get_all_category(db)
