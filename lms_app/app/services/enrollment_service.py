from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository


class EnrollmentService:
    def __init__(
        self,
        enrollment_repo: EnrollmentRepository,
        student_repo: StudentRepository,
        course_repo: CourseRepository
    ):
        self.enrollment_repo = enrollment_repo
        self.student_repo = student_repo
        self.course_repo = course_repo

    def enroll_student(self, enrollment_data: dict):
        student = self.student_repo.get_by_id(enrollment_data["student_id"])
        if not student:
            raise ValueError("Student not found")

        course = self.course_repo.get_by_id(enrollment_data["course_id"])
        if not course:
            raise ValueError("Course not found")

        if self.enrollment_repo.exists(
            enrollment_data["student_id"],
            enrollment_data["course_id"]
        ):
            raise ValueError("Already enrolled")

        return self.enrollment_repo.create(enrollment_data)

    def list_enrollments(self):
        return self.enrollment_repo.list_all()

    def list_by_student(self, student_id: int):
        return self.enrollment_repo.list_by_student(student_id)

    def list_by_course(self, course_id: int):
        return self.enrollment_repo.list_by_course(course_id)