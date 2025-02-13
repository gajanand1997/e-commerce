from passlib.context import CryptContext

# Initialize the password hashing context with bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def hash_password(password: str) -> str:
    """
    Hashes a plain text password using bcrypt.
    
    :param password: The plain text password to be hashed.
    :return: The hashed password as a string.
    """
    return pwd_context.hash(password)

# Function to verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if the provided plain text password matches the stored hashed password.
    
    :param plain_password: The plain text password input by the user.
    :param hashed_password: The stored hashed password.
    :return: True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
