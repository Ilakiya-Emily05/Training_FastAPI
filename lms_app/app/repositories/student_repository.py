class StudentRepository:
    def __init__(self):
        self._students = []
        self._id_counter = 1

    def create(self, student_data: dict):
        student = {
            "id": self._id_counter,
            "name": student_data["name"],
            "email": student_data["email"]
        }
        self._students.append(student)
        self._id_counter += 1
        return student

    def get_by_id(self, student_id: int):
        return next((s for s in self._students if s["id"] == student_id), None)

    def get_by_email(self, email: str):
        return next((s for s in self._students if s["email"] == email), None)

    def list_all(self):
        return self._students