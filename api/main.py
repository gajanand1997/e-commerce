from fastapi import FastAPI
from api.routes import auth, users,categories,products,address,carts,reviews,orders
from api.database.connection import engine
from api.database.base import Base

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(categories.router, prefix="/categories", tags=["categories"])


app.include_router(products.router, prefix="/products", tags=["products"])


app.include_router(address.router, prefix="/address", tags=["address"])


app.include_router(carts.router, prefix="/cart", tags=["cart"])


app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])


app.include_router(orders.router, prefix="/orders", tags=["orders"])



