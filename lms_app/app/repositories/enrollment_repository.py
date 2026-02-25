class EnrollmentRepository:
    def __init__(self):
        self._enrollments = []
        self._id_counter = 1

    def create(self, enrollment_data: dict):
        enrollment = {
            "id": self._id_counter,
            "student_id": enrollment_data["student_id"],
            "course_id": enrollment_data["course_id"]
        }
        self._enrollments.append(enrollment)
        self._id_counter += 1
        return enrollment

    def exists(self, student_id: int, course_id: int) -> bool:
        return any(
            e for e in self._enrollments
            if e["student_id"] == student_id and e["course_id"] == course_id
        )

    def list_all(self):
        return self._enrollments

    def list_by_student(self, student_id: int):
        return [e for e in self._enrollments if e["student_id"] == student_id]

    def list_by_course(self, course_id: int):
        return [e for e in self._enrollments if e["course_id"] == course_id]