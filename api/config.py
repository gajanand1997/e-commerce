import os  # Importing the OS module to interact with the operating system
from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from a .env file

# Load environment variables from a .env file into the application
load_dotenv()

# Retrieve the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Retrieve the secret key used for cryptographic operations
SECRET_KEY = os.getenv("SECRET_KEY")

# Retrieve the algorithm used for encoding/decoding tokens
ALGORITHM = os.getenv("ALGORITHM")

# Retrieve the expiration time (in minutes) for access tokens
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
