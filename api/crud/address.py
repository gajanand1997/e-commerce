from sqlalchemy.orm import Session
from api.database.models.address import AAddress
from api.database.schemas.address import AAddressCreate
from datetime import datetime


def create_address(db: Session, address: AAddressCreate):
    created_at = address.created_at or datetime.utcnow()

    db_address = AAddress(
        user_id=address.user_id,
        state=address.state,
        city=address.city,
        address_line1=address.address_line1,
        address_line2=address.address_line2,
        pincode=address.pincode,
        complete_address=address.complete_address,
        created_at=address.created_at,
       

    )
    db.add(db_address)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_address)  # Refresh the user instance with the latest data from DB
    return db_address

# okk

def delete_address(db: Session, address_id: int):
     
    address = db.query(AAddress).filter(AAddress.id == address_id).first()
    if address:
        db.delete(address)
        db.commit()
        return {"success": True,"message": "address deleted successfully"}
    
    return {"success": False,"message": "address not found"}



def get_all_address(db: Session):
    """
    Fetches all address from the database.
    
    :param db: Database session.
    :return: A list of all address.
    """
    return db.query(AAddress).all()

