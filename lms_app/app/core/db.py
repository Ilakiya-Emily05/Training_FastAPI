from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository

student_repository = StudentRepository()
course_repository = CourseRepository()
enrollment_repository = EnrollmentRepository()