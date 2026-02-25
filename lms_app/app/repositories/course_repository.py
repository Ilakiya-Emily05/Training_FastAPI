class CourseRepository:
    def __init__(self):
        self._courses = []
        self._id_counter = 1

    def create(self, course_data: dict):
        course = {
            "id": self._id_counter,
            "title": course_data["title"],
            "duration": course_data["duration"]
        }
        self._courses.append(course)
        self._id_counter += 1
        return course

    def get_by_id(self, course_id: int):
        return next((c for c in self._courses if c["id"] == course_id), None)

    def list_all(self):
        return self._courses