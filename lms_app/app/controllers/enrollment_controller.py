from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse
from app.services.enrollment_service import EnrollmentService
from app.dependencies.dependencies import get_enrollment_service

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.post("", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(
    enrollment: EnrollmentCreate,
    service: EnrollmentService = Depends(get_enrollment_service)
):
    try:
        return service.enroll_student(enrollment.model_dump())
    except ValueError as e:
        msg = str(e)
        if msg == "Already enrolled":
            raise HTTPException(status_code=400, detail=msg)
        raise HTTPException(status_code=404, detail=msg)


@router.get("", response_model=list[EnrollmentResponse])
def list_enrollments(
    service: EnrollmentService = Depends(get_enrollment_service)
):
    return service.list_enrollments()