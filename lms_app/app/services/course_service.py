from app.repositories.course_repository import CourseRepository


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def create_course(self, course_data: dict):
        return self.course_repo.create(course_data)

    def get_course(self, course_id: int):
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise ValueError("Course not found")
        return course

    def list_courses(self):
        return self.course_repo.list_all()