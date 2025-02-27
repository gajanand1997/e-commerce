from sqlalchemy import Column, Integer, String,DateTime,func,ForeignKey
from api.database.connection import Base

class Carts(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    quantity=Column(Integer)
    created_at=Column(DateTime,default=func.now())

   