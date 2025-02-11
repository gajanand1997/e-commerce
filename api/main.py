from fastapi import FastAPI
from api.routes import auth, users
from api.database.connection import engine
from api.database.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
