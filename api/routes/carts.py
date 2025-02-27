from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.carts import CartsCreate, CartsResponse
from api.crud.carts import create_cart,delete_cart,get_all_carts
from typing import List




# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=CartsResponse)
def add(cart: CartsCreate, db: Session = Depends(get_db)):
 
    return create_cart(db,cart)


@router.delete("/delete/{cart_id}", response_model=dict)
def delete(cart_id: int, db: Session = Depends(get_db)):
    return delete_cart(db, cart_id)


@router.get("/all_carts", response_model=List[CartsResponse])
def list_carts(db: Session = Depends(get_db)):
    return get_all_carts(db)
