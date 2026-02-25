This project is a backend API for a Learning Management System (LMS) built using FastAPI and Clean Architecture principles.
The system is designed for an EdTech platform (similar to Udemy or Coursera) to manage courses, students, and enrollments in a scalable and structured way.
The application uses in-memory storage (V1.0) and follows strict separation of concerns to ensure maintainability and extensibility.

Features
The system allows:
Course Management
Create courses
View course details
List all available courses
Student Management
Register new students
Fetch student profiles
Enrollment Management
Enroll students into courses
Prevent duplicate enrollments
View all enrollments
View enrollments by student
View enrollments by course

Architecture Overview 
Client
↓
Controller Layer (API)
↓
Service Layer (Business Logic)
↓
Repository Layer (Data Access)
↓
In-Memory Storage


Project Structure
lms_app/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── student_model.py
│   │   ├── course_model.py
│   │   └── enrollment_model.py
│   │
│   ├── schemas/
│   │   ├── student_schema.py
│   │   ├── course_schema.py
│   │   └── enrollment_schema.py
│   │
│   ├── repositories/
│   │   ├── student_repository.py
│   │   ├── course_repository.py
│   │   └── enrollment_repository.py
│   │
│   ├── services/
│   │   ├── student_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   │
│   ├── controllers/
│   │   ├── student_controller.py
│   │   ├── course_controller.py
│   │   └── enrollment_controller.py
│   │
│   ├── dependencies/
│   │   └── dependencies.py
│   │
│   └── middleware/
│       └── cors.py
│
├── requirements.txt
└── README.md