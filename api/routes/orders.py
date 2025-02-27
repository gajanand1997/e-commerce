from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.orders import OrdersCreate, OrdersResponse
from api.crud.orders import create_orders,delete_orders,get_all_orders
from typing import List



# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=OrdersResponse)
def add(orders: OrdersCreate, db: Session = Depends(get_db)):
 
    return create_orders(db,orders)


@router.delete("/delete/{orders_id}", response_model=dict)
def delete(orders_id: int, db: Session = Depends(get_db)):
    return delete_orders(db, orders_id)



@router.get("/all_orders", response_model=List[OrdersResponse])
def list_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)





