from fastapi import APIRouter, Depends
from api.database.schemas.user import UserResponse
from api.token import get_current_user

# Creating an API router instance for handling user-related routes
router = APIRouter()

@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    """
    Retrieve the profile of the currently authenticated user.

    Args:
        current_user (UserResponse): The authenticated user obtained via dependency injection.

    Returns:
        UserResponse: The details of the logged-in user.
    """
    return current_user