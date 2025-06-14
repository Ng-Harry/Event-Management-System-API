from fastapi import APIRouter, HTTPException
from typing import List
from schemas.models import Registration, RegistrationCreate
from services.registration_service import RegistrationService
from routes.user_routes import user_service
from routes.event_routes import event_service

router = APIRouter(prefix="/registrations", tags=["registrations"])
registration_service = RegistrationService(user_service, event_service)

@router.post("/", response_model=Registration)
def create_registration(registration: RegistrationCreate):
    new_registration = registration_service.create_registration(registration)
    if not new_registration:
        raise HTTPException(
            status_code=400,
            detail="Registration failed. User may be inactive, event may be closed, or user already registered."
        )
    return new_registration

@router.get("/", response_model=List[Registration])
def get_registrations():
    return registration_service.get_all_registrations()

@router.get("/user/{user_id}", response_model=List[Registration])
def get_user_registrations(user_id: int):
    if not user_service.get_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return registration_service.get_user_registrations(user_id)

@router.patch("/{registration_id}/attend", response_model=Registration)
def mark_attendance(registration_id: int):
    registration = registration_service.mark_attendance(registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration

@router.get("/attended", response_model=List[str])
def get_users_with_attendance():
    return registration_service.get_users_with_attendance() 