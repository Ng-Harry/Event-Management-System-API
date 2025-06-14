from datetime import datetime
from typing import List, Optional, Dict
from schemas.models import Registration, RegistrationCreate, RegistrationResponse
from services.user_service import UserService
from services.event_service import EventService

class RegistrationService:
    def __init__(self, user_service: UserService, event_service: EventService):
        self.registrations: List[Registration] = []
        self._next_id = 1
        self.user_service = user_service
        self.event_service = event_service

    def _get_registration_response(self, registration: Registration) -> RegistrationResponse:
        user = self.user_service.get_user(registration.user_id)
        event = self.event_service.get_event(registration.event_id)
        return RegistrationResponse(
            registration_id=registration.id,
            username=user.name if user else "Unknown User",
            event_name=event.title if event else "Unknown Event",
            registration_date=registration.registration_date,
            attended=registration.attended
        )

    def create_registration(self, registration: RegistrationCreate) -> Optional[RegistrationResponse]:
        # Check if user exists and is active
        user = self.user_service.get_user(registration.user_id)
        if not user or not user.is_active:
            return None

        # Check if event exists and is open
        event = self.event_service.get_event(registration.event_id)
        if not event or not event.is_open:
            return None

        # Check if user is already registered
        if self._is_user_registered(registration.user_id, registration.event_id):
            return None

        new_registration = Registration(
            id=self._next_id,
            user_id=registration.user_id,
            event_id=registration.event_id,
            registration_date=datetime.now(),
            attended=False
        )
        self.registrations.append(new_registration)
        self._next_id += 1
        return self._get_registration_response(new_registration)

    def _is_user_registered(self, user_id: int, event_id: int) -> bool:
        return any(
            reg.user_id == user_id and reg.event_id == event_id
            for reg in self.registrations
        )

    def get_registration(self, registration_id: int) -> Optional[RegistrationResponse]:
        registration = next((reg for reg in self.registrations if reg.id == registration_id), None)
        return self._get_registration_response(registration) if registration else None

    def get_all_registrations(self) -> List[RegistrationResponse]:
        return [self._get_registration_response(reg) for reg in self.registrations]

    def get_user_registrations(self, user_id: int) -> List[RegistrationResponse]:
        return [self._get_registration_response(reg) for reg in self.registrations if reg.user_id == user_id]

    def mark_attendance(self, registration_id: int) -> Optional[RegistrationResponse]:
        registration = self.get_registration(registration_id)
        if registration:
            registration.attended = True
        return registration

    def get_attended_registrations(self) -> List[RegistrationResponse]:
        return [self._get_registration_response(reg) for reg in self.registrations if reg.attended]

    def get_users_with_attendance(self) -> List[str]:
        attended_user_ids = {reg.user_id for reg in self.registrations if reg.attended}
        attended_users = [self.user_service.get_user(user_id) for user_id in attended_user_ids]
        return [user.name for user in attended_users if user is not None] 