# 🚀 FastAPI Authentication Project

A simple and professional **FastAPI** project with user authentication, database models, and JWT-based authentication system.

## 📌 Features
- ✅ User Registration & Login with JWT authentication
- ✅ Secure password hashing using **bcrypt**
- ✅ Role-based access control (optional)
- ✅ FastAPI-powered API with automatic documentation
- ✅ Pydantic for data validation and serialization
- ✅ Database integration with SQLAlchemy

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
│   │── token.py            # JWT token generation & validation
│   │── crud.py             # Database operations (CRUD)
│   │── routes/             # API route handlers
│   │   │── auth.py         # Authentication routes (register, login)
│   │   │── users.py        # User-related routes
│── .env                    # Environment variables
│── requirements.txt        # Dependencies
│── README.md               # Project documentation

## 🚀 Installation & Setup

1. Clone the repository:
   git clone https://github.com/yourusername/fastapi-auth-project.git
   cd fastapi-auth-project

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set up the database:
   alembic upgrade head  # Run migrations if using Alembic

5. Run the FastAPI server:
   uvicorn api.main:app --reload

6. Open API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔑 Authentication Workflow
1. **Register a new user** via `/auth/register`
2. **Login to get a JWT token** via `/auth/login`
3. **Use JWT token** for protected routes by adding it to the `Authorization` header as: `Bearer <token>`

## 📌 API Endpoints

| Method | Endpoint        | Description |
|--------|----------------|-------------|
| POST   | `/auth/register` | Register a new user |
| POST   | `/auth/login`    | Authenticate user and return JWT token |

## 📜 Environment Variables (.env)
```ini
DATABASE_URL=sqlite:///./test.db  # Change for PostgreSQL, MySQL, etc.
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🛠 Built With
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, high-performance web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database interactions
- [JWT](https://jwt.io/) - JSON Web Tokens for authentication
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and serialization

## 📌 Future Enhancements
- ✅ Role-based access control (RBAC)
- ✅ Refresh token implementation
- ✅ Email verification system

## 🤝 Contributing
Feel free to fork the repository and submit pull requests. Suggestions and contributions are welcome!

---
Happy coding! 🚀

