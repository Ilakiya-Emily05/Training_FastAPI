from fastapi import FastAPI

from app.controllers.student_controller import router as student_router
from app.controllers.course_controller import router as course_router
from app.controllers.enrollment_controller import router as enrollment_router
from app.middleware.cors import setup_cors

app = FastAPI(title="Learning Management System API")

setup_cors(app)

app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)