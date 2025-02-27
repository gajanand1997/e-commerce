from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.reviews import ReviewsCreate, ReviewsResponse
from api.crud.reviews import create_reviews,delete_reviews,get_all_reviews
from typing import List



# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=ReviewsCreate)
def add(reviews: ReviewsCreate, db: Session = Depends(get_db)):
 
    return create_reviews(db,reviews)


@router.delete("/delete/{reviews_id}", response_model=dict)
def delete(reviews_id: int, db: Session = Depends(get_db)):
    return delete_reviews(db, reviews_id)


@router.get("/all_reviews", response_model=List[ReviewsResponse])
def list_reviews(db: Session = Depends(get_db)):
    return get_all_reviews(db)
