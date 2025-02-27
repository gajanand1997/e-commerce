from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.user import UserCreate, UserLogin, UserResponse
from api.crud.user import create_user, get_user_by_email
from api.security import verify_password
from fastapi.security import OAuth2PasswordBearer
from api.token import create_access_token

# Create a new API router for handling authentication-related endpoints
router = APIRouter()

# Define OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to register a new user.
    
    - Checks if the email is already registered.
    - If not, creates a new user in the database.
    """
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Endpoint for user login.
    
    - Validates user credentials.
    - If correct, generates an access token.
    """
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Generate an access token for authenticated user
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}