
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.address import AAddressCreate, AAddressResponse
from api.crud.address import create_address,delete_address,get_all_address
from typing import List



# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=AAddressResponse)
def add(address: AAddressCreate, db: Session = Depends(get_db)):
 
    return create_address(db,address)


@router.delete("/delete/{address_id}", response_model=dict)
def delete(address_id: int, db: Session = Depends(get_db)):
    return delete_address(db, address_id)



@router.get("/all_address", response_model=List[AAddressResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_address(db)