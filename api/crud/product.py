from sqlalchemy.orm import Session
from api.database.models.products import Products
from api.database.schemas.products import ProductsCreate
from datetime import datetime


def create_product(db: Session, product: ProductsCreate):
    created_at = product.created_at or datetime.utcnow()

    db_product = Products(
        category_id=product.category_id,
        name=product.name,
        description=product.description,
        mrp=product.mrp,
        net_price=product.net_price,
        quantity_in_stock=product.quantity_in_stock,
        image=product.image,
        created_at=product.created_at,
        updated_at=product.updated_at ,
       
    )
    db.add(db_product)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_product)  # Refresh the user instance with the latest data from DB
    return db_product

# okk

def delete_product(db: Session, product_id: int):
     
    product = db.query(Products).filter(Products.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"success": True,"message": "product deleted successfully"}
    
    return {"success": False,"message": "product not found"}




def get_all_products(db: Session):
    """
    Fetches all products from the database.
    
    :param db: Database session.
    :return: A list of all products.
    """
    return db.query(Products).all()