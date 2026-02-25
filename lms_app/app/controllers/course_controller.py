from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.services.course_service import CourseService
from app.dependencies.dependencies import get_course_service

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(
    course: CourseCreate,
    service: CourseService = Depends(get_course_service)
):
    return service.create_course(course.model_dump())


@router.get("", response_model=list[CourseResponse])
def list_courses(
    service: CourseService = Depends(get_course_service)
):
    return service.list_courses()


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    service: CourseService = Depends(get_course_service)
):
    try:
        return service.get_course(course_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))