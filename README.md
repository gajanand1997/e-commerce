# 🚀 FastAPI Authentication Project

A simple and professional **FastAPI** project with user authentication, database models, and JWT-based login system.

## 📁 Project Structure

fastapi_project/
│── api/                  
│   │── main.py             # FastAPI entry point
│   │── config.py           # Configuration settings
│   │── database/           # Database-related files
│   │   │── connection.py   # Database connection setup
│   │   │── models/         # Models folder (separate models)
│   │   │   │── user.py     # User model
│   │   │   │── product.py  # Example of another model
│   │   │── schemas/        # Pydantic schemas folder
│   │   │   │── user.py     # User schema
│   │   │   │── product.py  # Product schema
│   │   │── base.py         # Base model for imports
│   │── security.py         # Password hashing & authentication
│   │── token.py            # To generate toekn
│   │── crud.py             # Database operations (CRUD)
│   │── routes/             # API route handlers
│   │   │── auth.py         # Authentication routes (register, login)
│   │   │── users.py        # User-related routes
│── .env                    # Environment variables
│── requirements.txt        # Dependencies
│── README.md               # Project documentation


pip install -r .\requirements
uvicorn api.main:app --reload
http://127.0.0.1:8000/docs