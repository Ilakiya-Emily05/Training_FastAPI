from app.repositories.student_repository import StudentRepository


class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def create_student(self, student_data: dict):
        existing = self.student_repo.get_by_email(student_data["email"])
        if existing:
            raise ValueError("Student with this email already exists")

        return self.student_repo.create(student_data)

    def get_student(self, student_id: int):
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return student

    def list_students(self):
        return self.student_repo.list_all()