from sqlalchemy.orm import Session
from api.database.models.orders import Orders
from api.database.schemas.orders import OrdersCreate
from datetime import datetime

def create_orders(db: Session, orders: OrdersCreate):
    created_at = orders.created_at or datetime.utcnow()

    db_orders = Orders(
        user_id=orders.user_id,
        subtotal=orders.subtotal,
        discount=orders.discount,
        total=orders.total,
        status=orders.status,
        shipping_address=orders.shipping_address,
        created_at=orders.created_at,
        updated_at=orders.updated_at ,
       
    )
    db.add(db_orders)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_orders)  # Refresh the user instance with the latest data from DB
    return db_orders

# okk

def delete_orders(db: Session, orders_id: int):
     
    orders = db.query(Orders).filter(Orders.id == orders_id).first()
    if orders:
        db.delete(orders)
        db.commit()
        return {"success": True,"message": "orders deleted successfully"}
    
    return {"success": False,"message": "orders not found"}




def get_all_orders(db: Session):
    """
    Fetches all orders from the database.
    
    :param db: Database session.
    :return: A list of all orders.
    """
    return db.query(Orders).all()