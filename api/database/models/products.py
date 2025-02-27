from sqlalchemy import Column, Integer, Float,String,DateTime,func,ForeignKey
from api.database.connection import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    # category_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), index=True)  # ForeignKey referencing categories table

    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    mrp=Column(Float)
    net_price=Column(Float)
    quantity_in_stock=Column(Integer)
    image = Column(String(100), nullable=False)
    created_at=Column(DateTime,default=func.now())
    updated_at = Column(DateTime, nullable=True)    

   