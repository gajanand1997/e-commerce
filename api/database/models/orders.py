from sqlalchemy import Column, Integer, String,DateTime,func,ForeignKey,Float,Enum
from api.database.connection import Base
from enum import Enum as PyEnum



# Enum to define the possible statuses
class OrderStatus(PyEnum):
    pending = "pending"
    shipped = "shipped"
    cancelled = "cancelled"
    delivered = "delivered"

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    subtotal=Column(Integer)
    discount=Column(Float)
    total=Column(Float)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending) 
     # Enum field for status
    shipping_address=Column(String(100), nullable=False)
    created_at=Column(DateTime,default=func.now())
    updated_at = Column(DateTime, nullable=True)    

   