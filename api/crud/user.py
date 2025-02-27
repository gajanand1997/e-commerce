from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate

from api.security import hash_password


# Function to create a new user in the database
def create_user(db: Session, user: UserCreate):
    """
    Creates a new user with hashed password and stores it in the database.
    
    :param db: Database session.
    :param user: User data from the request.
    :return: The newly created user object.
    """
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),  # Hash the password before storing
        mob_number=user.mob_number,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
        
    )
    db.add(db_user)  # Add the user to the database session
    db.commit()  # Commit the transaction to save changes
    db.refresh(db_user)  # Refresh the user instance with the latest data from DB
    return db_user

# Function to retrieve a user by email
def get_user_by_email(db: Session, email: str):
    """
    Fetches a user from the database using their email.
    
    :param db: Database session.
    :param email: User's email address.
    :return: User object if found, else None.
    """
    return db.query(User).filter(User.email == email).first()

# Function to retrieve a user by ID
def get_user_by_id(db: Session, user_id: int):
    """
    Fetches a user from the database using their unique ID.
    
    :param db: Database session.
    :param user_id: User's unique identifier.
    :return: User object if found, else None.
    """
    return db.query(User).filter(User.id == user_id).first()