from sqlalchemy import Column, Integer, String,DateTime,func,ForeignKey,CheckConstraint
from api.database.connection import Base

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    rating = Column(Integer, CheckConstraint('rating >= 1 AND rating <= 5'), nullable=False)  # Rating between 1 and 5
    review=Column(Integer)
    created_at=Column(DateTime,default=func.now())

   