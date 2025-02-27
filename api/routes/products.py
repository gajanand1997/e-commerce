from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.products import ProductsCreate, ProductsResponse
from api.crud.product import create_product,delete_product, get_all_products
from typing import List



# Create a new API router for handling authentication-related endpoints
router = APIRouter()


@router.post("/add" , response_model=ProductsResponse)
def add(product: ProductsCreate, db: Session = Depends(get_db)):
 
    return create_product(db,product)

@router.get("/all_products", response_model=List[ProductsResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)




@router.delete("/delete/{product_id}", response_model=dict)
def delete(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)