Banking Loan Management System (LMS) Backend
Overview
This project implements a scalable and enterprise-ready Banking Loan Management System (LMS)** backend using FastAPI, PostgreSQL, and SQLAlchemy. It follows a Clean Architecture with proper separation of concerns (Controller → Service → Repository) and includes transactional integrity, pagination, dependency injection, and middleware for security and logging.

The system supports:
- Customer loan applications
- Loan officer review and approval
- Admin management of loan products
- Repayment tracking
- Secure and reliable operations for enterprise usage

Features
- User Management: Create, read, update, delete users
- Loan Product Management: CRUD operations with pagination
- Loan Applications: Apply, approve/reject, view status
- Repayments: Add repayments, view history, close loans
- Middleware: CORS, logging
- Exception Handling: Centralized custom exceptions
- Clean Architecture: Controller → Service → Repository
- Database: PostgreSQL with SQLAlchemy ORM & Alembic migrations

Technology Stack
- **Python 3.11+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM (v2)**
- **Pydantic**
- **Alembic**
- **Uvicorn** (for running the server)

Folder Structure
banking_lms/
│
├── app/
│   ├── main.py                      # FastAPI entrypoint
│   │
│   ├── core/
│   │   ├── config.py                # Settings
│   │   ├── database.py              # SQLAlchemy engine/session
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── loan_product.py
│   │   ├── loan_application.py
│   │   └── repayment.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   ├── application_schema.py
│   │   └── repayment_schema.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   ├── application_repository.py
│   │   └── repayment_repository.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   ├── application_service.py
│   │   └── repayment_service.py
│   │
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── product_controller.py
│   │   ├── application_controller.py
│   │   └── repayment_controller.py
│   │
│   ├── middleware/
│   │   ├── cors.py
│   │   └── logging_middleware.py
│   │
│   └── exceptions/
│       ├── custom_exceptions.py
│       └── exception_handlers.py
│
├── alembic/
├── alembic.ini
├── requirements.txt
└── README.md