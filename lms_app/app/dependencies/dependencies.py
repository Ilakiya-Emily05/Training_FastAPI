from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository

from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

student_repository = StudentRepository()
course_repository = CourseRepository()
enrollment_repository = EnrollmentRepository()

def get_student_service():
    return StudentService(student_repository)

def get_course_service():
    return CourseService(course_repository)

def get_enrollment_service():
    return EnrollmentService(
        enrollment_repository,
        student_repository,
        course_repository
    )