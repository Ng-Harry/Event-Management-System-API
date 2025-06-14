from datetime import datetime
from typing import List, Optional
from schemas.models import Registration, RegistrationCreate
from services.user_service import UserService
from services.event_service import EventService

class RegistrationService:
    def __init__(self, user_service: UserService, event_service: EventService):
        self.registrations: List[Registration] = []
        self._next_id = 1
        self.user_service = user_service
        self.event_service = event_service

    def create_registration(self, registration: RegistrationCreate) -> Optional[Registration]:
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
        return new_registration

    def _is_user_registered(self, user_id: int, event_id: int) -> bool:
        return any(
            reg.user_id == user_id and reg.event_id == event_id
            for reg in self.registrations
        )

    def get_registration(self, registration_id: int) -> Optional[Registration]:
        return next((reg for reg in self.registrations if reg.id == registration_id), None)

    def get_all_registrations(self) -> List[Registration]:
        return self.registrations

    def get_user_registrations(self, user_id: int) -> List[Registration]:
        return [reg for reg in self.registrations if reg.user_id == user_id]

    def mark_attendance(self, registration_id: int) -> Optional[Registration]:
        registration = self.get_registration(registration_id)
        if registration:
            registration.attended = True
        return registration

    def get_attended_registrations(self) -> List[Registration]:
        return [reg for reg in self.registrations if reg.attended]

    def get_users_with_attendance(self) -> List[int]:
        attended_user_ids = {reg.user_id for reg in self.registrations if reg.attended}
        return list(attended_user_ids) 