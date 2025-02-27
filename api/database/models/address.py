from sqlalchemy import Column, Integer, String,DateTime,func,ForeignKey
from api.database.connection import Base

class AAddress(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address_line1 = Column(String(100), nullable=False)
    address_line2 = Column(String(100), nullable=False)
    pincode=Column(Integer)
    complete_address = Column(String(100), nullable=False)
    created_at=Column(DateTime,default=func.now())

   