from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService
from app.dependencies.dependencies import get_student_service

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(
    student: StudentCreate,
    service: StudentService = Depends(get_student_service)
):
    try:
        return service.create_student(student.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    service: StudentService = Depends(get_student_service)
):
    try:
        return service.get_student(student_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))