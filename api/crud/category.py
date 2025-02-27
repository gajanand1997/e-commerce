from sqlalchemy.orm import Session
from api.database.models.categories import Categories
from api.database.schemas.categories import CategoryCreate
from datetime import datetime



def create_category(db: Session, category: CategoryCreate):
    created_at = category.created_at or datetime.utcnow()

    db_category = Categories(
        name=category.name,
        created_at=category.created_at,
        updated_at=category.updated_at 
       
    )
    db.add(db_category)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_category)  # Refresh the user instance with the latest data from DB
    return db_category

# okk

def delete_category(db: Session, category_id: int):
     
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return {"success": True,"message": "Category deleted successfully"}
    
    return {"success": False,"message": "Category not found"}



def get_all_category(db: Session):
    """
    Fetches all category from the database.
    
    :param db: Database session.
    :return: A list of all category.
    """
    return db.query(Categories).all()