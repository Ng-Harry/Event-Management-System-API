from typing import List, Optional
from schemas.models import Event, EventCreate

class EventService:
    def __init__(self):
        self.events: List[Event] = []
        self._next_id = 1

    def create_event(self, event: EventCreate) -> Event:
        new_event = Event(
            id=self._next_id,
            title=event.title,
            location=event.location,
            date=event.date,
            is_open=True
        )
        self.events.append(new_event)
        self._next_id += 1
        return new_event

    def get_event(self, event_id: int) -> Optional[Event]:
        return next((event for event in self.events if event.id == event_id), None)

    def get_all_events(self) -> List[Event]:
        return self.events

    def update_event(self, event_id: int, event_data: EventCreate) -> Optional[Event]:
        event = self.get_event(event_id)
        if event:
            event.title = event_data.title
            event.location = event_data.location
            event.date = event_data.date
        return event

    def delete_event(self, event_id: int) -> bool:
        event = self.get_event(event_id)
        if event:
            self.events.remove(event)
            return True
        return False

    def close_event(self, event_id: int) -> Optional[Event]:
        event = self.get_event(event_id)
        if event:
            event.is_open = False
        return event

    def get_open_events(self) -> List[Event]:
        return [event for event in self.events if event.is_open] 