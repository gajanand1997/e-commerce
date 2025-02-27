from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from api.config import SECRET_KEY, ALGORITHM
from api.crud.user import get_user_by_email
from api.database.connection import get_db
from sqlalchemy.orm import Session

# Define the OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    """
    Generates a JWT access token with an expiration time.
    
    :param data: Dictionary containing user information to encode in the token.
    :param expires_delta: Time duration for which the token remains valid (default is 30 minutes).
    :return: Encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})  # Add expiration time to the token payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to retrieve the currently authenticated user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Decodes the JWT token to extract user information and validate authentication.
    
    :param token: JWT token retrieved from the request header.
    :param db: Database session dependency.
    :return: Authenticated user object.
    """
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # Extract email from token payload
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception  # Handle invalid token errors
    
    # Fetch user details from the database
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception  # Raise exception if user not found
    return user