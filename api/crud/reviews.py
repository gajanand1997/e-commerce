
from sqlalchemy.orm import Session
from api.database.models.reviews import Reviews
from api.database.schemas.reviews import ReviewsCreate
from datetime import datetime


def create_reviews(db: Session, reviews: ReviewsCreate):
    created_at = reviews.created_at or datetime.utcnow()

    db_reviews = Reviews(
        user_id=reviews.user_id,
        order_id=reviews.order_id,
        product_id=reviews.product_id,
        rating=reviews.rating,
        review=reviews.review,
        created_at=reviews.created_at,
       
    )
    db.add(db_reviews)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_reviews)  # Refresh the user instance with the latest data from DB
    return db_reviews

# okk

def delete_reviews(db: Session, reviews_id: int):
     
    reviews = db.query(Reviews).filter(Reviews.id == reviews_id).first()
    if reviews:
        db.delete(reviews)
        db.commit()
        return {"success": True,"message": "reviews deleted successfully"}
    
    return {"success": False,"message": "reviews not found"}





def get_all_reviews(db: Session):
    """
    Fetches all reviews from the database.
    
    :param db: Database session.
    :return: A list of all reviews.
    """
    return db.query(Reviews).all()